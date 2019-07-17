# -*- coding: utf-8 -*-

import abc
import datetime
import uuid

from astraeus.models.memcache import MemcacheClientBuilder, MemcacheFacade
from astraeus.models.mongodb import MongoDBBuilder


class Hasher:
    """ Something that hashes something """

    @abc.abstractmethod
    def hash_key(self, key):
        return 0


class UUIDHasher(Hasher):
    """ Hashing based on UUID4 """

    def hash_key(self, key):
        hashed = str(uuid.uuid4())
        hashed = hashed.replace('-', '')
        return hashed


class Astraeus(object):
    """ Saves in-memory data about stuff """

    MEMCACHE_PORT = 11211  # default memcache port
    EXPIRE_SECONDS = ((60 * 60) * 24) * 14  # 14 days

    def __init__(self,
                 port=MEMCACHE_PORT,
                 expire_seconds=EXPIRE_SECONDS,
                 hash_function=UUIDHasher().hash_key):
        """
        :param port: port where memcache runs
        :param expire_seconds: values in memcache will be null after that
        :param hash_function: function to compute hash of key
        """

        client = MemcacheClientBuilder() \
            .with_server('localhost') \
            .with_port(port) \
            .build()

        self.memcache = MemcacheFacade(client, expire_seconds)
        self.hasher = hash_function  # function to hash stuff

    def _get_key(self, val):
        return self.hasher(str(val))  # todo better jsonify ?

    def save(self, val):
        """
        :param val: Saves val in memcache database
        :return: key of memcache
        """

        assert not (val is None)

        key = self._get_key(val)
        if self.memcache.set(key, val):
            return key

        return None

    def retrieve(self, key):
        assert not (key is None)

        return self.memcache.get(key)


class MongoAstraeus(Astraeus):
    """ Normal Astraeus, but saves data also in MongoDB for reduncancy
    reasons """

    MONGO_DB = 'astraeus'  # todo move to config

    def _get_parent(self):
        return super(self.__class__, self)

    def __init__(self,
                 mongo_collection,
                 mongo_db=MONGO_DB,
                 port=Astraeus.MEMCACHE_PORT,
                 expire_seconds=Astraeus.EXPIRE_SECONDS,
                 hash_function=UUIDHasher().hash_key):
        super(self.__class__, self).__init__(port, expire_seconds, hash_function)

        mongo = MongoDBBuilder() \
            .with_db(mongo_db) \
            .build()
        self.mongo = mongo[mongo_collection]  # specify collection

    def _try_save_to_memcache(self, val):
        try:
            return self._get_parent().save(val)
        except:
            print 'Cannot save {} to memcache'.format(val)

        return None

    def _try_save_to_mongodb(self, memcache_key, val):
        if not memcache_key:
            memcache_key = self._get_key(val)

        try:
            item = self.build_mongo_item(memcache_key, val)
            self.mongo.insert_one(item)
            return memcache_key
        except:
            print 'Cannot save {} to mongodb'.format(val)

        return None

    def save(self, val):
        key = self._try_save_to_memcache(val)  # first save to memcache ...
        key = self._try_save_to_mongodb(key, val)  # ... then in mongo
        return key

    def _try_retrieve_from_memcache(self, key):
        try:
            return self._get_parent().retrieve(key)
        except:
            print 'Cannot retrieve {} from memcache'.format(key)

        return None

    def _try_retrieve_from_mongodb(self, key):
        try:
            results = self.mongo.find({'key': key})
            if results:
                most_recent = max(results, key=lambda x: x['time'])  # sort by date
                return most_recent['val']  # DO NOT check expiration: this is a redundant database
        except:
            print 'Cannot retrieve {} from mongodb'.format(key)

        return None

    def retrieve(self, key):
        val = self._try_retrieve_from_memcache(key)  # first try with memcache ...
        if not val:
            return self._try_retrieve_from_mongodb(key)  # ... then with mongo

        return val

    @staticmethod
    def build_mongo_item(key, val):
        time_now = datetime.datetime.now()
        return {
            'key': key,
            'val': val,
            'time': time_now
        }

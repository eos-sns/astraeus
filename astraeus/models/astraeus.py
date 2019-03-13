# -*- coding: utf-8 -*-

import abc
import uuid

from astraeus.models.memcache import MemcacheClientBuilder, MemcacheFacade


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


class Astraeus:
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

        self.client = MemcacheClientBuilder() \
            .with_server('localhost') \
            .with_port(port) \
            .build()

        self.memcache = MemcacheFacade(self.client, expire_seconds)
        self.hasher = hash_function  # function to hash stuff

    def save(self, val):
        """
        :param val: Saves val in memcache database
        :return: key of memcache
        """

        key = self.hasher(str(val))
        if self.memcache.set(key, val):
            return key

        return None

    def retrieve(self, key):
        return self.memcache.get(key)

# -*- coding: utf-8 -*-

from core import MongoAstraeus


def main():
    mongo_coll = 'wow'
    astraeus_client = MongoAstraeus(mongo_coll)

    to_save = 'wooooooooooooooooooooooow'
    key = astraeus_client.save(to_save)
    if not key:
        print 'Cannot save {}'.format(to_save)
    else:
        print 'saved {} with key {}'.format(to_save, key)
        print 'retrieve({}) -> {}'.format(key, astraeus_client.retrieve(key))


if __name__ == '__main__':
    main()

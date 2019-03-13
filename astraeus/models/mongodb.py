# -*- coding: utf-8 -*-

""" Interface for pymongo """

from pymongo import MongoClient


class MongoDBBuilder:
    def __init__(self):
        self.client = MongoClient()
        self.db_name = ''

    def with_db(self, db):
        self.db_name = db
        return self

    def build(self):
        return self.client[self.db_name]

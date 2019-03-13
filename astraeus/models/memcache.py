# -*- coding: utf-8 -*-

""" Interface for pymemcache """

from pymemcache.client.base import Client


class MemcacheFacade:
    def __init__(self, client, expire_seconds):
        self.client = client
        self.expire_seconds = expire_seconds

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value):
        return self.client.set(key, value, expire=self.expire_seconds)


class MemcacheClientBuilder:
    def __init__(self):
        self.server = 'localhost'
        self.port = 11211  # default memcache port

    def with_server(self, server):
        self.server = server
        return self

    def with_port(self, port):
        self.port = port
        return self

    def build(self):
        return Client((self.server, self.port))

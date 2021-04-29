#!/usr/bin/python3
""" MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Create a class MRUCache that inherits
    from BaseCaching and is a caching system:
    """
    
    def __init__(self):
        super().__init__()
        self.head, self.tail = '-', '='
        self.next, self.prev = {}, {}
        self.__group(self.head, self.tail)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.__remove(key)
            self.__add(key, item)
#!/usr/bin/env python3
"""Cache replacement policies - FIFO"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Cache replacement policies - FIFO"""

    def __init__(self):
        """initialize cache_data"""
        super().__init__()

    def put(self, key, item):
        """insert new item and discard the first item if
        len(cache_data) > BaseCaching.MAX_ITEMS"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = next(iter(self.cache_data))
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """get cache_data"""
        return self.cache_data.get(key)

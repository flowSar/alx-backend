#!/usr/bin/env python3
"""Cache replacement policies - LIFO"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """Cache replacement policies - LIFO"""

    def __init__(self):
        """initialize cache_data"""
        super().__init__()

    def put(self, key, item):
        """insert new item and discard the last item if
        len(cache_data) > BaseCaching.MAX_ITEMS"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = list(self.cache_data.keys())[-1]
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """get cache_data"""
        if key is not None:
            return self.cache_data.get(key)
        return None

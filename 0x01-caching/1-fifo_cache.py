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
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.cache_data.get(key) is None:
                    first_key = list(self.cache_data.keys())[0]
                    del self.cache_data[first_key]
                    self.cache_data[key] = item
                    print('DISCARD: ', first_key)

            self.cache_data[key] = item

    def get(self, key):
        """get cache_data"""
        if key is not None:
            return self.cache_data.get(key)
        return None

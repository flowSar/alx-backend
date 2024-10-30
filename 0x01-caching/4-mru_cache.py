#!/usr/bin/env python3
"""Cache replacement policies - MRU"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """Cache replacement policies - MRU"""

    def __init__(self):
        """initialize cache_data"""
        super().__init__()

    def put(self, key, item):
        """insert new item and discard the MRU when
        len(cache_data) > BaseCaching.MAX_ITEMS"""
        if key and item:
            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                last = self.cache_data.popitem()
                print('DISCARD: ', last[0])
                
            self.cache_data[key] = item

    def get(self, key):
        """get cache_data"""
        if key is not None:
            return self.cache_data.get(key)
        return None

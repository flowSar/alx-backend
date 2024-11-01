#!/usr/bin/env python3
"""Cache replacement policies - LRUCache"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Cache replacement policies - LRUCache"""

    def __init__(self):
        """initialize cache_data"""
        super().__init__()

    def put(self, key, item):
        """insert new item and discard the least recently used  if
        len(cache_data) > BaseCaching.MAX_ITEMS"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.order.pop(0)
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """get cache_data"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)


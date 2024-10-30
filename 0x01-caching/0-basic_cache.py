#!/usr/bin/env python3
"""module for caching"""


class BasicCache(BaseCaching):
    """override BaseCaching function in BasicCache"""

    def __init__(self):
        """initialize cache_data"""
        super().__init__()

    def put(self, key, item):
        """insert new item to cache_data"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get cache_data"""
        if key is not None:
            return self.cache_data.get(key)
        return None

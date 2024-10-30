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
                if self.cache_data.get(key) is None:
                    last = self.cache_data.popitem()
                    self.cache_data[key] = item
                    print('DISCARD: ', last[0])

            self.cache_data[key] = item

    def get(self, key):
        """get cache_data"""
        if key is not None:
            return self.cache_data.get(key)
        return None

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()

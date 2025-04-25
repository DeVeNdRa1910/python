# Impliment a decorator that caches the return values of a function, so that when its called with the same arguments, the cached value is returned instead of re-executing the function.

import time 
def cache(func):
    cache_values = {}
    def wrapper(*args, **kwargs):
        if args in cache_values:
            return cache_values[args]
        result = func(*args, **kwargs)
        cache_values[args] = result
        return result
    return wrapper

@cache
def add(a, b):
    time.sleep(4)
    return a+b

print(add(123523, 546235))
print(add(123523, 546235))
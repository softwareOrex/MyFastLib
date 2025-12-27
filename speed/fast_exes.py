from functools import lru_cache

def fast_cache(max_size=128):
    def decorator(func):
        return lru_cache(maxsize=max_size)(func)
    return decorator

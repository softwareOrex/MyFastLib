import functools


def cached(func):
cache = {}
@functools.wraps(func)
def wrapper(*args):
if args in cache:
return cache[args]
result = func(*args)
cache[args] = result
return result
return wrapper

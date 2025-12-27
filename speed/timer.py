import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[MyFastLib] {func.__name__} executed in {end - start:.6f}s")
        return result
    return wrapper

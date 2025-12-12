import time
from concurrent.futures import ThreadPoolExecutor
from functools import wraps


def timer(func):
"""Декоратор для измерения времени выполнения функции."""
@wraps(func)
def wrapper(*args, **kwargs):
start = time.time()
result = func(*args, **kwargs)
end = time.time()
print(f"Время выполнения: {end - start:.6f} секунд")
return result
return wrapper


def batch(iterable, size):
"""Разбивает последовательность на батчи фиксированного размера."""
for i in range(0, len(iterable), size):
yield iterable[i:i+size]


def parallel_map(func, data, workers=4):
"""Параллельное применение функции к итерируемым данным с помощью ThreadPoolExecutor."""
with ThreadPoolExecutor(max_workers=workers) as ex:
return list(ex.map(func, data))

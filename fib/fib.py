#!/usr/bin/env python3
from time import time
from functools import wraps

def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return func(*args, **kwargs)
    return wrapper


@benchmark
def fib(num):
    a, b = 0, 1
    c = []
    while a < num:            # First iteration:
        c.append(a)            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)
    return c



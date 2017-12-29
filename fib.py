from time import time
from functools import wraps

def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        rval = func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t) 
        return rval
    return wrapper


def fib_rec_memo(n, hash = {0:1, 1:1}):
    if n not in hash:
        hash[n] = fib_rec_memo(n-1) + fib_rec_memo(n-2)
    return hash[n]


def fib_standard(num):
    a, b = 0, 1
    c = []
    while a < num:            # First iteration:
        c.append(a)            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)
    return c




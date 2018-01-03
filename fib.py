from time import time
from functools import wraps
import click

@click.command()
@click.argument('num')
@click.option('--bench', default=False, help='Benchmark fibonacci number with decorator.')
@click.option('--type', default='standard', type=click.Choice(['standard', 'recursive']),  help='Standard or recursive (w/ memoization)')
def launch_fib(num, fib_type='standard', bench=False):
    print(num)
    print(bench)
    print(fib_type)
    if type == 'standard':
        x = 0
        while x < num:
            print(fib_standard(num))
            x += 1
    if type == 'recursive':
        x = 0
        while x < num:
            print(fib_rec_memo(x))
            x += 1


def benchmark(func, condition=False):
    if not condition:
        return None

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

        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)
    return a


if __name__ == '__main__':
    launch_fib()

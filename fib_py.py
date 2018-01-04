from time import time
from functools import wraps
import click
import cProfile
from fib_standard import fib_standard
from fib_recursive import fib_rec_memo

@click.command()
@click.argument('num')
@click.option('--bench', default=False, help='Benchmark fibonacci number with decorator.')
@click.option('--type', default='standard', type=click.Choice(['standard', 'recursive']),  help='Standard or recursive (w/ memoization)')
def launch_fib(num, bench=False, type='standard'):
    i = int(num)
    if type == 'standard' and bench == True:
        cProfile.runctx('fib_std(i)', globals=globals(), locals=dict(i=i))
    else:
        fib_std(i)
    if type == 'recursive' and bench == True:
        cProfile.runctx('fib_rec(i)', globals=globals(), locals=dict(i=i))
    else:
        fib_rec(i)

def fib_std(num):
    for x in range(num):
        print(fib_standard(x))

def fib_rec(num):
    x = 0
    while x < num:
        print(fib_rec_memo(x))
        x += 1


if __name__ == '__main__':
    launch_fib()

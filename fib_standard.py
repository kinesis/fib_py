from fib import benchmark, fib_standard 

@benchmark
def print_fib(n):
    print(fib_standard(n))

print_fib(100)

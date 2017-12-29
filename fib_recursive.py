from fib import benchmark, fib_rec_memo

@benchmark
def print_fib(n):
    for x in range(0, n):
        print(fib_rec_memo(x))

print_fib(10)


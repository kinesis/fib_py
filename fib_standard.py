from fib import benchmark, fib_standard 
import sys, argparse



if len(sys.argv[1]) == 2:
    if sys.argv[1] == "--bench":
        print("bench")
    else:
        if int(sys.argv[1]) 

@benchmark
def print_fib(n):
    x = 1
    while x < n:
        print(fib_standard(x))
        x += 1

print_fib(int(sys.argv[1]))

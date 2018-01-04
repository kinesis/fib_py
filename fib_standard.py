def fib_standard(num):
    fibs = [0, 1]
    for i in range(2, num+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[-1]


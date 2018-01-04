def fib_rec_memo(n, hash = {0:1, 1:1}):
    if n not in hash:
        hash[n] = fib_rec_memo(n-1) + fib_rec_memo(n-2)
    return hash[n]

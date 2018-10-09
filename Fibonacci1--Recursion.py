def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# change the "30" to whatever positive integer you'd like it to calculate up to.
for i in range(1, 30):
    print (fib(i))

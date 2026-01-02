def nth_fibonacci(n):
    a, b = 0,1

    for _ in range(n-1):
        a, b = b, a+b
    
    return a

    #0 based indexing or 1based indexing would decide if to use "n-1" or "n", and returning a or b is just working

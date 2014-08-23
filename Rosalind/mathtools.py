def generalized_fib(n, k):
    a, b = 0, 1
    counter = 0
    while counter < n-1:    # need to subtract one since the initialization
                            # ate up a generation
        a, b = b, k*a + b
        counter += 1

    return b


if __name__ == '__main__':
    print generalized_fib(5, 3)

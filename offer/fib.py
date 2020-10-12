def get_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        import numpy as np
        res = np.zeros((n+1),dtype = np.int)
        res[0] = 0
        res[1] = 1
        for i in range(2,n+1):
            res[i] = res[i-1]+res[i-2]
            res[i] = int(res[i] % (1e9 + 8) + res[i] // (1e9 + 8))
        return res[n]


if __name__ == '__main__':
    n = 5
    res = get_fib(n)
    res = int(res)
    print(type(res))
    # res = int(res % (1e9 + 7) + res // (1e9 + 7))
    print(res)
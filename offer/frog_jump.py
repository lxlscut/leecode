

def nums_ways(n):
    # 只有一阶台阶时

    if n == 1:
        return 1
    # 台阶数为0时
    elif n == 0:
        return 0
    # 有二阶台阶时
    elif n == 2:
        return 2
    else:
        import numpy as np
        res = np.zeros((n+1,),dtype=np.int)
        res[0] = 1
        res[1] = 1
        res[2] = 2
        for i in range(3,n+1):
            res[i] = res[i-2] + res[i-1]
            if res[i]//(1e9+7):
                res[i] = 1
        return res[n]

if __name__ == '__main__':
    res = nums_ways(0)
    print(res)
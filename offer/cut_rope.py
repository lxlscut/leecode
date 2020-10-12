def cut_rope(length):
    max = 0
    # cut成m段
    for i in range(2, length + 1):
        # 取整数部分
        a = length // i
        # 取余数部分
        b = length % i
        val = a**(i-b)*(a+1)**b
        if val>max:
            max = val
    return max

if __name__ == '__main__':
    res = cut_rope(2)
    print(res)

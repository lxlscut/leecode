import sys

sys.setrecursionlimit(9000000)  # 这里设置大一些


def find_maxmun_crossmid_subarray(a, low, mid, high):  # 使用分治法寻找最大和子序列，第三种情况
    left_sum = -float('inf')
    right_sum = -float('inf')
    sum = 0
    i = mid
    while i >= low:
        sum = sum + a[i]
        if sum >= left_sum:
            left_sum = sum
            left_max = i
        i = i - 1

    sum = 0
    j = mid + 1
    while j <= high:
        sum = sum + a[j]
        if sum >= right_sum:
            right_sum = sum
            right_max = j
        j = j + 1
    return [left_max, right_max, left_sum + right_sum]


def find_maxmun_subarray(a, low, high):  # 使用分治法寻找最大和子序列
    print(low,high)
    r = []
    l = []
    m = []  # 将序列分为三部分，其最大和子序列会存在于三者之间
    if low == high:
        return [low, high, a[low]]
    else:
        mid = (low + high) / 2
        l = find_maxmun_subarray(a, low, mid)
        r = find_maxmun_subarray(a, mid + 1, high)
        m = find_maxmun_crossmid_subarray(a, low, mid, high)  # 如果存在于前半部分或者后半部分，将问题分治，如果包含中间，则使用另一个线性函数处理
        if l[2] >= r[2] and l[2] >= m[2]:
            return l
        elif r[2] >= l[2] and r[2] >= m[2]:
            return r
        else:
            return m  # 判断最大和子序列的范围

if __name__ == '__main__':
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    find_maxmun_subarray(a, 0, 10)
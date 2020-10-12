import math
import sys
sys.setrecursionlimit(9000000)  # 这里设置大一些

def crosses_max(A, low, mid, high):
    print(low,high)
    max_left = 0
    left_index = 0
    for i in range(mid, low-1, -1):
        if max_left < max_left + A[i]:
            max_left = max_left + A[i]
            left_index = i
    max_right = 0
    right_index = high
    for j in range(mid + 1, high):
        if max_right < max_right + A[j]:
            max_right = max_right + A[j]
            right_index = j
    max_cross = max_right + max_left

    return [left_index, right_index, max_cross]


def sub_max(A, low, high):
    if low == high-1:
        return [low, high, A[low]]
    mid = math.floor((low + high) / 2)
    left_low, left_high, max_left = sub_max(A, low, mid)
    right_low, right_high, max_right = sub_max(A, mid+1, high)
    cross_low, cross_high, max_cross = crosses_max(A, low, mid, high)
    if max_left >= max_right and max_left >= max_cross:
        return left_low, left_high, max_left
    elif max_right >= max_left and max_right >= max_cross:
        return right_low, right_high, max_right
    else:
        return cross_low, cross_high, max_cross


if __name__ == '__main__':
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sub_max(a, 0, 9)

    # crosses_max(a, 0, 3, 5)

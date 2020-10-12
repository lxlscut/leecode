import numpy as np
import time

# 机器人的行走必须是连续的
def robot(m, n, k):
    """
    :param m: 方格的宽
    :param n: 方格的高
    :param k: 高宽之和限制值
    :return:
    """
    """数位之和不能大于k"""
    if m + n == 0:
        return 0
    else:
        matrix = np.ones((m, n), dtype=np.int)
        go_next_step(0, 0, matrix, k, 0)
        steps = m*n - np.sum(matrix)
        return steps


def go_next_step(start0, start1, matrix, k, num):
    # print(start0, start1)
    # 首先找到其四邻域
    if k < canculate_bit_sum(start0, start1):
        return
    up, down, left, right = find_neighbor(matrix, start0, start1)
    matrix[start0, start1] = 0
    if up == 1:
        # if k >= canculate_bit_sum(start0 - 1, start1):
        go_next_step(start0 - 1, start1, matrix, k, num)
    if down == 1:
        # if k >= canculate_bit_sum(start0 + 1, start1):
        go_next_step(start0 + 1, start1, matrix, k, num)
    if left == 1:
        # if k >= canculate_bit_sum(start0, start1 - 1):
        go_next_step(start0, start1 - 1, matrix, k, num)
    if right == 1:
        # if k >= canculate_bit_sum(start0, start1 + 1):
        go_next_step(start0, start1 + 1, matrix, k, num)
    return


def find_neighbor(matrix, i, j):
    up, down, left, right = None, None, None, None
    if 0 <= i - 1:
        up = matrix[i - 1][j]
    if i + 1 < len(matrix):
        down = matrix[i + 1][j]
    if 0 <= j - 1:
        left = matrix[i][j - 1]
    if j + 1 < len(matrix[0]):
        right = matrix[i][j + 1]
    return up, down, left, right


def canculate_bit_sum(m, n):
    a = str(m)
    b = str(n)
    sum = 0
    for i in a:
        sum = sum + (ord(i) - ord('0'))
    for j in b:
        sum = sum + (ord(j) - ord('0'))
    return sum


if __name__ == '__main__':
    res = robot(20, 23, 8)
    print(res)

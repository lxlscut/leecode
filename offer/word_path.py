import copy
import time
def find_path(matrix, word):
    if matrix[0][0] == None or len(word) == 0:
        return False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == word[0]:
                # 开始寻找路径
                # matrix_copy = copy.deepcopy(matrix)
                res = find_with_start(matrix,i,j,word,1)
                if res== True:
                    return res
    return False



def find_with_start(matrix,i,j,word,num):
    """
    :param matrix: 矩阵
    :param i: 起点的行数
    :param j: 起点的列数
    :param word: 词语
    :param num: 当前的编号
    :return:
    """
    # 如果已走完
    if num == len(word):
        return True
    # 防止走回头路
    temp = matrix[i][j]
    matrix[i][j] = None
    target = word[num]
    up, down, left, right = find_neighbor(matrix,i,j)
    if up == target:
        res1 = find_with_start(matrix,i-1,j,word,num+1)
        if res1==True:
            return True
    if down == target:
        res2 = find_with_start(matrix,i+1,j,word,num+1)
        if res2==True:
            return True
    if left == target:
        res3 = find_with_start(matrix,i,j-1,word,num+1)
        if res3==True:
            return True
    if right == target:
        res4 = find_with_start(matrix,i,j+1,word,num+1)
        if res4==True:
            return True
    matrix[i][j] = temp
    return False



# def find_with_start(matrix,i,j,word,num):
#     """
#     :param matrix: 矩阵
#     :param i: 起点的行数
#     :param j: 起点的列数
#     :param word: 词语
#     :param num: 当前的编号
#     :return:
#     """
#     # 如果已走完
#     if num == len(word):
#         return True
#
#     # 防止走回头路
#     temp = matrix[i][j]
#     matrix[i][j] = None
#     target = word[num]
#
#     up, down, left, right = find_neighbor(matrix,i,j)
#     if up == target:
#         copy_up = copy.deepcopy(matrix)
#         res1 = find_with_start(copy_up,i-1,j,word,num+1)
#         # matrix[i][j]=temp
#         if res1==True:
#             return True
#     if down == target:
#         copy_down = copy.deepcopy(matrix)
#         res2 = find_with_start(copy_down,i+1,j,word,num+1)
#         # matrix[i][j] = temp
#         if res2==True:
#             return True
#     if left == target:
#         copy_left = copy.deepcopy(matrix)
#         res3 = find_with_start(copy_left,i,j-1,word,num+1)
#         # matrix[i][j] = temp
#         if res3==True:
#             return True
#     if right == target:
#         copy_right = copy.deepcopy(matrix)
#         res4 = find_with_start(copy_right,i,j+1,word,num+1)
#         # matrix[i][j] = temp
#         if res4==True:
#             return True
#     # matrix[i][j] = temp
#     return False






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


if __name__ == '__main__':
    board = [["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]]
    word = "aaaa" \
           "aaaa" \
           "aaaaa"

    start = time.time()
    res = find_path(board, word)
    end = time.time()
    print(res)
    print(end-start)
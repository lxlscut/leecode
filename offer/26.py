def spiralOrder(matrix):
    res = []
    # 计算出矩阵的高于宽
    height = len(matrix)
    width = len(matrix[0])
    start_x = 0
    start_y = 0
    while start_x<=width and start_y<=height:
        for i in range(start_x, width):
            res.append(matrix[start_y][i])
        start_y += 1
        for j in range(start_y, height):
            res.append(matrix[j][width - 1])
        width -= 1
        for k in range(width - 1, start_x-1,-1):
            res.append(matrix[height - 1][k])
        height -= 1
        for l in range(height - 1, start_y-1,-1):
            res.append(matrix[l][start_x])
        start_x += 1

    return res[:len(matrix)*len(matrix[0])]


if __name__ == '__main__':
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    res = spiralOrder(matrix)
    print(res)
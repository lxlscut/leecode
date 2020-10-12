import pprint
import copy
def get_island(input):
    final_result = 0
    for i in range(len(input)):
        for j  in range(len(input[i])):
            # 找到一个起点
            if(input[i][j] ==0):
                input[i][j] = 1
                result = find_4_neighbor(i,j,input)
                if result == 0:
                    final_result += 1
    return final_result

# 寻找四个领域的值
def find_4_neighbor(start0,start1,input):

    flag0=0
    flag1=0
    flag2=0
    flag3=0
    try:
        if input[start0][start1 + 1] == 0:
            input[start0][start1 + 1] = 1
            flag0 = find_4_neighbor(start0, start1 + 1, input)
    except Exception as e:
        flag0=1
        pass
    try:
        if input[start0 + 1][start1] == 0:
            input[start0 + 1][start1] = 1
            flag1 = find_4_neighbor(start0 + 1, start1, input)
    except Exception  as e:
        flag1=1
        pass

    try:
        if input[start0 - 1][start1] == 0  and  (start0-1)>=0:
            input[start0 - 1][start1] = 1
            flag2 = find_4_neighbor(start0 - 1, start1, input)
        if  (start0 - 1) < 0:
            flag2 = 1
    except Exception as e:
        flag2=1
        pass

    try:
        if input[start0][start1 - 1] == 0  and  (start1-1)>=0:
            input[start0][start1 - 1] = 1
            flag3 = find_4_neighbor(start0, start1 - 1, input)
        elif  (start1-1)<0:
            flag3 = 1
    except Exception as e:
        flag3 = 1
        pass

    return flag0+flag1+flag2+flag3


if __name__ == '__main__':
    grid =[[0,1,1,1,1,1,1,1],
           [1,0,1,0,0,0,0,1],
           [1,0,0,0,0,1,0,1],
           [0,1,0,0,0,1,0,1],
           [1,0,0,1,0,1,0,1],
           [1,1,1,1,0,0,1,1],
           [1,0,0,0,0,0,1,1],
           [0,1,1,1,1,1,1,1]]
    result = get_island(grid)
    print(result)


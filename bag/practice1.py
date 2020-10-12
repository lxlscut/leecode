"""problem description:
the bag could stow 8 unit,and the information of item is:
num:1 2 3 4
val:2 3 4 5
vol:3 4 5 6
"""
import numpy as np

# use dynamic programming
def get_max_item(volume,value,n):
    """
    :param volumn: the volume of these items
    :param value: the value of these items
    :param n: the volume of the bag
    :return:
    """
    result = np.zeros((len(value),n+1),dtype=np.int)
    result[0,:] = 3
    result[:,0] = 0
    result[:,1] = 0
    for i in range(1,len(value)):
        for j in range(2,n+1):
            vol = volume[i]
            if vol>j:
                result[i, j] = result[i-1,j]
            elif vol <= j:
                a = value[i] + result[i-1,j-volume[i]]
                b = result[i-1,j]
                result[i, j] = max(a,b)
    return result



if __name__ == '__main__':
    volume = [2,3,4,5]
    value =  [3,4,5,6]
    result = get_max_item(volume,value,8)
    print(result)
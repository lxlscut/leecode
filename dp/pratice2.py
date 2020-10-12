"""problem description:
    test if a array has a subset which sum is the appointed value
"""
import numpy as np

# use recursion
def find_subset(nums,n,value):
    current_value = nums[n]
    if n>=0 and (current_value==value or value==0):
        return True
    elif n == 0 and current_value != value:
        return False
    elif current_value>value:
        return find_subset(nums,n-1,value)
    elif current_value<value:
        a = find_subset(nums,n-1,value-current_value)
        b = find_subset(nums,n-1,value)
        return a or b

# use dynamic programming
def find_subset1(nums,n,value):
    result = np.zeros((n,value+1),dtype=np.bool)
    print(result.shape)
    result[:,0] = False
    result[0,:] = False
    result[0,3] = True
    for i in range(1, n):
        for j in range(1,value+1):
            current_value = nums[i]
            if current_value>j:
                result[i,j] = result[i-1,j]
            elif current_value<j:
                A = result[i-1,j-current_value]
                B = result[i-1,j]
                result[i,j] = A or B

    return result[-1,-1]


if __name__ == '__main__':
    nums = [3,34,4,12,5,2]
    n = len(nums)-1
    a = find_subset(nums,n,65)
    print(a)
    n = len(nums)
    a = find_subset1(nums,n,65)
    print(a)

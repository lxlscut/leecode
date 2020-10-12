import numpy as np
"""find the biggest sum value of the item which are not neighbor to each other"""


# use dynamic programming
def find_sum(nums):
    opt = np.zeros(len(nums))
    opt[0] = nums[0]
    opt[1] = nums[1]
    for i in range(2,len(nums)):
        a = nums[i] + opt[i-2]
        b = opt[i-1]
        opt[i] = max(a,b)

    return opt[len(nums)-1]


# use recursion
def find_sum1(nums,n):
    if n==0:
        return nums[0]
    elif n==1:
        return nums[1]
    else:
        a = nums[n] + find_sum1(nums,n-2)
        b = find_sum1(nums,n-1)
        value = max(a,b)
        return value


if __name__ == '__main__':
    nums = [1, 2, 4, 1, 7, 8, 3]
    result = find_sum1(nums,len(nums)-1)
    print(result)
    result1 = find_sum(nums)
    print(result1)

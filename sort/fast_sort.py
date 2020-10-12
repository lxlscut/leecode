def my_sort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            m=nums[i]
            n=nums[j]
            if m>n:
                nums[i] = n
                nums[j] = m
    return nums






if __name__ == '__main__':
    nums = [1, 8, 6, 2, 5, 4, 9, 3, 7]
    nums = my_sort(nums)
    print(nums)
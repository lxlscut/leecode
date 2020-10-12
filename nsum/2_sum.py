def tow_sum(nums,target):
    nums = sorted(nums)
    low = 0
    high = len(nums)-1
    while low<high:
        sum = nums[low]+nums[high]
        if sum<target:
            if nums[low] == nums[low+1]:
                continue
            low+=1
        elif sum>target:
            if nums[high]==nums[high-1]:
                continue
            high -= 1
        else:
            break

    if low==high:
        return -1
    else:
        return nums[low],nums[high]



if __name__ == '__main__':
    nums = [1, 3, 2, 6]
    target = 9
    [low,high] = tow_sum(nums,target)
    print(low,high)
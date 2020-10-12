def solution(nums):
    size = len(nums)
    mid = size // 2
    while mid >= 1:
        for i in range(mid, size):
            temp = nums[i]
            j = i - mid
            while j >= 0 and nums[j] > temp:
                nums[j+mid] = nums[j]
                j=j-mid
            nums[j+mid] = temp
        mid = mid//2
    return nums


if __name__ == '__main__':
    a = [5, 4, 38, 1]
    print(solution(a))
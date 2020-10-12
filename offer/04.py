def find_num(nums, target):
    if target < nums[0][0] or target > nums[-1][-1]:
        return False
    for i in nums:
        while target >= i[-1]:
            i += 1
        for j in i:
            if target ==  j:
                return True
    return False


if __name__ == '__main__':
    nums = [[1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]]
    target = 50
    res = find_num(nums, target)
    print(res)

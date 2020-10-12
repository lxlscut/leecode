def permute(nums):
    res = []
    def track_back(nums,num):
        if not nums:
            res.append([num])
            return
        for i in range(len(nums)):
            track_back(nums[:i]+nums[i+1:], num+[nums[i]])

    track_back(nums,[])

    return res



if __name__ == '__main__':
    a = [1, 2, 3]
    result = permute(a)
    print(result)

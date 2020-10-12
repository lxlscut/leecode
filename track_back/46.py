
def get_full_permutation(nums):
    res = []
    res = track_back(nums,[],res)
    return res
def track_back(nums,tmp,res):
    if not nums:
        res.append(tmp)
        return
    for i in range(len(nums)):
        track_back(nums[:i]+nums[i+1:],tmp+[nums[i]],res)
    return res




if __name__ == '__main__':
    nums = [1,2,3]
    res = get_full_permutation(nums)
    print(res)
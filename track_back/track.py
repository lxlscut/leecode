import copy
def back(res,nums,track):
    """
    :param res: 最终的结果
    :param nums: 当前可以选择的路线
    :param track: 当前的路径
    :return:
    """
    # 一条路径走完，必然有track路径的长度与原始nums的长度相等
    if len(nums) == len(track):
        res.append(copy.deepcopy(track))
        return

    # 对nums里面的每一个元素进行遍历
    for i in range(len(nums)):
        if nums[i] in track:
            continue
        track.append(nums[i])
        back(res,nums,track)
        track.pop()
    return res

if __name__ == '__main__':
    nums = [1,2,3,4]
    res = []
    track = []
    res = back(res, nums, track)
    print(res)
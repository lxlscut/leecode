import copy


"""我们要意识到用了某个数字的话说明对于该数字的排列已经全部被用了，因此我们要将其排除"""
"""we need to make it clear that once the number been choose,
then any combination of the number will be find out in the relevant iteration"""
def three_sum(nums, target):
    final_result = []
    nums = sorted(nums)
    initial = nums[0]
    for i in range(len(nums)):
        subt = nums.pop(0)
        if subt==initial and i>0:
            continue
        else:
            initial = subt
        new_target = target - subt
        res = tow_sum(nums, new_target)
        if not res == None:
            for k in res:
                final_result.append([subt, k[0], k[1]])
    return final_result


def tow_sum(nums, target):
    low = 0
    high = len(nums) - 1
    res = []
    while low < high:
        sum = nums[low] + nums[high]
        if sum < target:
            while low < high and nums[low] == nums[low + 1]:
                low += 1
            low += 1

        elif sum > target:
            while low < high and nums[high] == nums[high - 1]:
                high -= 1
            high -= 1
        elif sum == target:
            res.append([nums[low], nums[high]])
            while low < high and nums[low] == nums[low + 1]:
                low += 1
            low+=1
            while low < high and nums[high] == nums[high - 1]:
                high -= 1
            high-=1

    return res





# def three_sum_new(nums, target):
#     final_result = []
#     nums = sorted(nums)
#
#     for i in range(len(nums)):
#         subt = nums.pop(0)
#
#         new_target = target - subt
#         res = tow_sum(nums, new_target)
#         if not len(res) == 0:
#             for k in res:
#                 final_result.append([subt, k[0], k[1]])
#     return final_result


if __name__ == '__main__':
    nums = [0,0,0]
    target = 0
    a = three_sum(nums, target)
    print(a)

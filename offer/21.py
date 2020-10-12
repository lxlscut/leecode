def exchange( nums):
    back_index = len(nums) - 1
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            while nums[back_index] % 2 == 0:
                back_index -= 1
            swap(nums[i], nums[back_index])
    return nums


def swap(self, a, b):
    temp = a
    a = b
    b = temp
    return
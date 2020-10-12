
def my_sort(nums, low, high,k):
    if low < high:
        mid, nums = partition_sort(nums, low, high)
        if mid>k:
            nums = my_sort(nums, low, mid - 1,k)
        elif mid<k:
            nums = my_sort(nums, mid + 1, high,k)
        elif mid == k:
            return nums
    # print(nums)
    return nums


def partition_sort(nums, low, high):
    base = nums[low]
    while (low < high):
        while (low < high and nums[high] <= base):
            high -= 1
        nums = swap(low, high, nums)
        while (low < high and nums[low] >= base):
            low += 1
        nums = swap(low, high, nums)
    return low, nums


def swap(a, b, nums):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
    return nums


# todo 寻找第K个大的值并不需要将所有的值都排序
def get_k(nums, k):
    initial_low = 0
    initial_high = len(nums) - 1
    nums = my_sort(nums, initial_low, initial_high,k-1)
    print(nums)
    return nums[k-1]

if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = get_k(nums, 4)
    print(k)
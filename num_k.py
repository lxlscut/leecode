def get_num(nums,k):
    initial_low = 0
    initial_high = len(nums)-1
    nums = my_sort(nums,initial_low,initial_high)
    print(nums)
    return nums[k]



def my_sort(nums,low,high):
    if low<high:
        mid,nums = partition_sort(nums,low,high)
        nums = my_sort(nums,low,mid-1)
        nums = my_sort(nums,mid+1,high)
    return nums


def partition_sort(nums,low,high):
    base = nums[low]
    print("excuting ... ")
    while (low<high):
        while (low<high and nums[high]>=base):
            high -= 1
        nums = swap(low,high,nums)
        while (low<high and nums[low]<=base):
            low+=1
        nums = swap(low,high,nums)
    return low,nums

def swap(a,b,nums):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
    return nums





if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = get_num(nums,4)
    print(k)
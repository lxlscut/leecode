def find_index(nums,num,start,end):
    mid = (start+end)//2
    while True:
        if start==end-1 and nums[start]!= num and nums[end]!=num:
            return -1

        elif nums[mid]>num:
            #那么在前半部分
            return find_index(nums,num,start,mid)
        elif nums[mid]<num:
            return find_index(nums,num,mid,end)
        elif nums[mid]==num:
            return mid







if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    num = 13
    res = find_index(nums,num,0,len(nums))
    print(res)

"""父节点：（i-1）//2,子节点:（2*i+1）"""
def swap(a,b,nums):
    a_value = nums[a]
    b_value = nums[b]
    nums[a] = b_value
    nums[b] = a_value
    return nums


def heapify(nums,n):
    """
    :param nums: 数组
    :param n: 节点序号
    :return:
    """
    son1 = 2*n+1
    son2 = 2*n+2
    length = len(nums)
    max = n
    if (son1<length and nums[max]<nums[son1]):
        max = son1
    if (son2<length and nums[max]<nums[son2]):
        max = son2
    if not max==n:
        swap(max,n,nums)
        heapify(nums,max)

    return nums


def build_heap(num):
    length = len(num)
    last_node = length-1
    last_parent = (last_node-1)//2
    for i in range(last_parent,-1,-1):
        num = heapify(num,i)
    return num

def sort_heap(heap):

    pass

if __name__ == '__main__':
    num = [2,5,3,1,10,4]
    num = heapify(num,0)
    print(num)
    num = build_heap(num)
    print(num)
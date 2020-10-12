def judge(postorder):
    if len(postorder)<=1:
        return True
    root = postorder[-1]
    index = len(postorder)
    for i in range(len(postorder)):
        if postorder[i]>root:
            index = i
            print(i)
            break
    for i in range(index,len(postorder),1):
        if  postorder[i]<root:
            return False
    if index==len(postorder):
        return judge(postorder[:index-1])
    return judge(postorder[:index]) and judge(postorder[index:len(postorder)-1])


if __name__ == '__main__':
    postorder = [4, 6, 7, 5]
    print(sum(postorder))
    res = judge(postorder)
    print(res)

def find(s):
    firstTime = [-1 for _ in range(26)]
    lastTime = [-1 for _ in range(26)]

    for i, char in enumerate(s):
        cIdx = ord(char) - ord('a')
        if firstTime[cIdx] == -1:
            firstTime[cIdx] = i
        lastTime[cIdx] = i

    sortLast = [i for i in lastTime if i != -1]
    sortLast.sort()  # 对右端点升序排序

    ans = []
    end = -1
    for last in sortLast:  # 每种字符最后出现的位置 升序遍历
        k = last  # k指向last处字符最后出现的位置
        first = firstTime[ord(s[k]) - ord('a')]  # first指向last处字符第一次出现的位置
        while first < k:  # 从k往first遍历
            cIdx = ord(s[k]) - ord('a')
            if lastTime[cIdx] > last or k <= end:
                break  # 需要向右扩展 或向左扩展时与前面的线段重叠了 就退出
            first = min(first, firstTime[cIdx])  # 向左扩展
            k -= 1  # k往左遍历
        if k == first:  # 扩展完毕，且当前线段不重叠也不需要向右扩展
            ans.append(s[first:last + 1])
            end = last
    return ans




if __name__ == '__main__':
    s = ["a","d","e","f","a","d","d","a","c","c","c"]
    print(find(s))



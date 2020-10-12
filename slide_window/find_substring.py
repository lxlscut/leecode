import collections
def slide_window(S,T):
    need = collections.defaultdict(int)
    for c in T:
        need[c] += 1
    needCnt = len(T)
    i=0
    res = (0,float('inf'))
    for j,c in enumerate(S):
        # j向右移动
        if need[c]>0:
            needCnt -= 1
        need[c] -= 1
        # i也向右移动，缩小边界
        if needCnt==0:
            while True:
                c = S[i]
                # 不能再向右移动了
                if need[c] == 0:
                    break
                need[c]+=1
                i+=1
            # 获取结果，准确来说是最小的最合适的结果
            if j-i<res[1]-res[0]:
                res = (i,j)
            # 接着找下一个最佳的值
            need[S[i]] += 1
            needCnt += 1
            i+=1
    return "" if res[1]>len(S) else S[res[0]:res[1]+1]

def minWindow(s, t):
    # 利用一个map来统计当前的需求
    import collections
    need_num = collections.defaultdict(int)
    for c in t:
        need_num[c] += 1
    # 一共需要多少个字母
    need_total = len(t)
    # 初始化下标
    res = (0, float("inf"))
    # i从0开始
    i = 0
    for j, c in enumerate(s):

        if need_num[c] > 0:
            need_num[c] -= 1
            need_total -= 1
        else:
            need_num[c] -= 1

        # 所有的都已经找齐了，我们开始移动i
        if need_total == 0:
            while True:
                c1 = s[i]
                if need_num[c1] == 0:
                    break
                else:
                    need_num[c1] += 1
                i += 1
            if j - i < res[1] - res[0]:
                res = (i, j)

            need_num[s[i]] += 1
            need_total += 1
            i += 1
    print(res)
    return "" if res[1] > len(s) else s[res[0]:res[1] + 1]





if __name__ == '__main__':
    S = "a"
    T = "aa"
    res = minWindow(S,T)
    print(res)

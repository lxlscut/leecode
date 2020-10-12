def checkInclusion(s1,s2):
    import collections
    need_total = len(s1)
    need_num = collections.defaultdict(int)
    for c in s1:
        need_num[c] += 1

    # 开始寻找
    i = 0
    for j, c in enumerate(s2):
        if need_num[c] > 0:
            need_num[c] -= 1
            need_total -= 1
        else:
            need_num[c] -= 1
        # 开始移动i
        if need_total == 0:
            while True:
                c1 = s2[i]
                if need_num[c1] == 0:
                    break
                else:
                    need_num[c1] += 1
                i += 1
            if j - i + 1 == len(s1):
                return True
            else:
                need_num[s2[i]] += 1
                need_total += 1
                i += 1
    return False

if __name__ == '__main__':
    s1 = "ky"
    s2 = "ainwkckifykxlribaypk"
    res = checkInclusion(s1,s2)
    print(res)
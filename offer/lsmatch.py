def isMatch(s,p):
    if not p:
        print(s)
        print(not s)
        return not s
    # 第一个字母是否匹配
    first_match = bool(s and p[0] in {s[0],'.'})
    # 如果 p 第二个字母是 *
    if len(p) >= 2 and p[1] == "*":
        return isMatch(s, p[2:]) or \
        first_match and isMatch(s[1:], p)
    else:
        return first_match and isMatch(s[1:], p[1:])



if __name__ == '__main__':
    s = "aa"
    p = "a*"
    print(isMatch(s,p))
    print("LLLLLL")
    print(not "A")
    print(not None)


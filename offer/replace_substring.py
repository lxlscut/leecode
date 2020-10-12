def replace_string(s):
    ss = ""
    for i in s:
        if i == " ":
            ss = ss+"%20"
        else:
            ss = ss+i
    return ss

if __name__ == '__main__':
    s = "We are happy."
    res = replace_string(s)
    print(res)
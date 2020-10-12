def remove(l, val):
    if not l:
        return
    count = 0
    for i in range(len(l)):
        if l[i] != val:
            l[count] = l[i]
            count += 1
    return l, count



if __name__ == '__main__':
    a = [1, 2, 2, 3]
    val = 2
    l, count = remove(a, val)
    print(l)
    print(count)
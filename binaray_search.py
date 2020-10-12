def binary_search(n, val):

    while True:
        length = len(n)
        index = length // 2
        middle = n[index]
        if val > middle:
            binary_search(n[index:],val)
        elif val < middle:
            binary_search(n[:index],val)
        elif val == middle or len(n) == 1:
            break
    return index




if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    b = binary_search(a,3)
    print(b)
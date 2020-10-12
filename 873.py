def find_longest(n):
    s = set(n)

    result = 0
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            a, b = n[i], n[j]
            count = 2
            while a+b in s:
                a, b = b, a+b
                count += 1
                result = max(result,count)

    return  result


if __name__ == '__main__':
    a = find_longest([1,2,3,4,5,6,7,8,9])
    print(a)




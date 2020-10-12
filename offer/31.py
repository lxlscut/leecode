def pop_push(push,pop):
    if push==[] and pop==[]:
        return True
    a = pop.pop(0)
    if pop==[]:
        if a==push[0] and len(push)==1:
            return True
        else:
            return False
    b = pop[0]

    index1 = push.index(a)
    index2 = push.index(b)
    print("index1:",index1,"a:",a)
    if index2==index1-1 or index2>index1:
        push.pop(index1)
        return pop_push(push,pop)
    else:
        return False


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    res = pop_push(pushed,popped)
    print(res)
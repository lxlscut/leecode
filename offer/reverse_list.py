# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
    next_node = head.next
    head.next = None
    while True:
        new_next_node = next_node.next
        next_node.next = head
        head = next_node
        next_node = new_next_node
        if new_next_node.next == None:
            new_next_node.next = head
            break
    return new_next_node


def printListFromTailToHead(listNode):
    list = []
    while listNode:
        list.insert(0, listNode.val)
        listNode = listNode.next
    return list




if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(1)
    c.next = None
    b.next = c
    a.next = b
    print(printListFromTailToHead(a))
    res = reverse_list(a)
    print(res.val)
    print(res.next.val)
    print(res.next.next.val)
    print(res.next.next.next)

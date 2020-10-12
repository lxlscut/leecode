import math
math.log(10,2)

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


def minDepth(root):
    if root == None:
        return 0
    queue = []
    queue.append(root)
    new_queue = []
    depth = 0
    while True:
        if len(queue)==0:
            if len(new_queue)==0:
                break
            else:
                queue = new_queue
                new_queue = []
                depth += 1
        else:
            node = queue.pop(0)
            new_queue,bb = process(node,new_queue)
            if bb==True:
                depth += 1
                break
    return depth

def process(node,queue):
    bb = False
    if not node.left == None:
        queue.append(node.left)
    if not node.right == None:
        queue.append(node.right)
    if node.left==None and node.right==None:
        bb = True
        return queue,bb
    return queue,bb



if __name__ == '__main__':
    # v15 = TreeNode(15)
    # v7 = TreeNode(7)
    # v20 = TreeNode(20)
    # v20.left = v15
    # v20.right = v7
    # v9 = TreeNode(9)
    # v3 = TreeNode(3)
    # v3.left = v9
    # v3.right = v20

    v5 = TreeNode(5)
    v4 = TreeNode(4)
    v3 = TreeNode(3)

    v3.right = v5
    v2 = TreeNode(2)
    v2.left = v4
    v1 = TreeNode(1)
    v1.left = v2
    v1.right = v3

    print(minDepth(v1))


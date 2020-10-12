class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def reconstruct_tree(preorder,inorder):
    return helper(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1)



def helper(preorder,inorder,left,right,left1,right1):
    if right>len(preorder)-1 or right1>len(inorder)-1 or left>right or left1>right1:
        return None
    else:
        # 获取根节点
        root = preorder[left]
        node = TreeNode(root)
        # 获取中序遍历中的位置
        root_index = inorder.index(root)
        count = root_index-left1
        # 左子树
        left_tree_left = left+1
        # left_tree_right = left+count+1
        left_tree_right = left + count
        left_tree_left1 = left1

        left_tree_right1 = root_index

        # 右子树
        right_tree_left = left+count+1
        right_tree_right = right
        right_tree_left1 = root_index+1
        right_tree_right1 = right1


        node.left = helper(preorder,inorder,left_tree_left,left_tree_right,left_tree_left1,left_tree_right1)
        node.right = helper(preorder,inorder,right_tree_left,right_tree_right,right_tree_left1,right_tree_right1)
        return node


if __name__ == '__main__':
    # 前序遍历
    preorder = [3, 9, 20, 15, 7]
    # 中序遍历
    inorder = [9, 3, 15, 20, 7]

    node = reconstruct_tree(preorder,inorder)
    print(preorder[1:1])

    # # print(inorder.index(20))
    # print(node.val)
    # print(node.left.val)
    # print(node.right.val)
    # print(node.right.right.val)
"""
操作给定的二叉树，将其变换为源二叉树的镜像。 输入描述:

二叉树的镜像定义：源二叉树
        8
       /  \
      6   10
     / \  / \
    5  7 9 11
    镜像二叉树
        8
       /  \
      10   6
     / \  / \
    11 9 7  5
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mirror(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    if root.left:
        mirror(root.left)
    if root.right:
        mirror(root.right)
"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def helper(tree_a, tree_b):
    if not tree_b:
        return True
    elif not tree_a:
        return False
    elif tree_a.val != tree_b.val:
        return False
    else:
        return helper(tree_a.left, tree_b.left) and helper(tree_a.right, tree_b.right)


def has_subtree(p_root1, p_root2):
    # write code here
    if not p_root1 or not p_root2:
        return False
    # 2 是不是 1的子树
    res = False
    if p_root1.val == p_root2.val:
        res = helper(p_root1, p_root2)
    if res:
        return True
    else:
        return has_subtree(p_root1.left, p_root2) or has_subtree(p_root1.right, p_root2)
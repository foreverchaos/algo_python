"""
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_btree_depth(pRoot):
    if not pRoot:
        return 0
    queue = [pRoot]
    count = 0
    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        count += 1
    return count


def print_depth(pRoot):
    if not pRoot:
        return 0
    left = print_depth(pRoot.left)
    right = print_depth(pRoot.right)
    return max(left, right) + 1
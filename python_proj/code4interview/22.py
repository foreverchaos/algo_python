"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_btree_layer(root):
    if not root:
        return []
    queue, result = [], []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


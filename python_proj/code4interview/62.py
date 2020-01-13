"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8） 中，按结点数值大小顺序第三小结点的值为4。
"""


def kth_node(pRoot, k):
    if not pRoot or k < 1:
        return None
    res = []

    def mid_order(node, res):
        if node is None:
            return
        mid_order(node.left, res)
        if len(res) == k:
            return
        else:
            res.append(node)
        mid_order(node.right, res)

    mid_order(pRoot, res)
    return res[-1] if k <= len(res) else None

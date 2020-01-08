class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left  # 左子树
        self.right = right  # 右子树


def pre_traverse(root):
    """
    前序遍历
    """
    if root is None:
        return
    print(root.value)
    pre_traverse(root.left)
    pre_traverse(root.right)


def pre_order(root):
    node, stack = root, []
    while node or stack:
        while node:
            stack.append(node)
            print(node.value)
            node = node.left
        node = stack.pop()
        node = node.right


def mid_traverse(root):
    """
    中序遍历
    """
    if root is None:
        return
    mid_traverse(root.left)
    print(root.value)
    mid_traverse(root.right)


def mid_order(root):
    node, stack = root, []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.value)
        node = node.right


def after_traverse(root):
    """
    后序遍历
    """
    if root is None:
        return
    after_traverse(root.left)
    after_traverse(root.right)
    print(root.value)


def after_order(root):
    node, stack = root, []
    while node or stack:
        while node:
            print(node.value)
            stack.append(node)
            node = node.right
        node = stack.pop()
        node = node.left


def layer_order(root):
    if root is None:
        return
    queue, results = [], []
    node = root
    queue.append(node)
    while queue:
        node = queue.pop(0)
        results.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return results


if __name__ == '__main__':
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
    print('前序遍历：')
    pre_traverse(root)
    print('\n')
    pre_order(root)
    print('\n')
    print('中序遍历：')
    mid_traverse(root)
    print('\n')
    print('后序遍历：')
    after_traverse(root)
    print('\n')


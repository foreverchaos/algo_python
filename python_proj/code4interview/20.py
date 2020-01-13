"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.min_data = []

    def push(self, node):
        self.stack.append(node)
        if not self.min_data:
            self.min_data.append(node)
        else:
            if self.min_data[-1] < node:
                self.min_data.append(self.min_data[-1])
            else:
                self.min_data.append(node)

    def pop(self):
        self.stack.pop()
        self.min_data.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_data[-1]








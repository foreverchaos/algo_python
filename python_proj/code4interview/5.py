"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


class SelfQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        for i in range(len(self.stack1)-1):
            self.stack2.append(self.stack1.pop())
        res = self.stack1.pop()
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return res


if __name__ == '__main__':
    s = SelfQueue()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.push(4)
    print(s.pop())
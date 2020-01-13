"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


def more_than_half_num_solution(numbers):
    if len(numbers) == 1:
        return numbers[0]
    nums_copy = []
    i, j = 0, 1
    while j < len(numbers):
        if numbers[i] == numbers[j]:
            nums_copy.append(numbers[i])
        i += 1
        j += 1
    if not nums_copy:
        return 0
    else:
        return nums_copy[0]


def more_than_half(numbers):
    if len(numbers) == 1:
        return numbers[0]
    stack = []
    temp = []
    for i in range(len(numbers)):
        if not stack or numbers[i] == stack[-1]:
            stack.append(numbers[i])
            if len(stack) > 1:
                temp.append(stack[-1])
        else:
            stack.pop()
    return stack[0] if stack and stack[0] in temp else 0


if __name__ == '__main__':
    n = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    n = [1, 2, 3, 2, 4, 2, 5, 2, 3]
    print(more_than_half(n))

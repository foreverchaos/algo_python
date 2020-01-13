"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""

from functools import cmp_to_key


def compare(s1, s2):
    if s1+s2 < s2+s1:
        return -1
    elif s1+s2 == s2+s1:
        return 0
    else:
        return 1


def print_min_number(numbers):
    # write code here
    if not numbers:
        return ''
    if len(numbers) == 1:
        return numbers[0]
    str_numbers = [str(n) for n in numbers]

    return ''.join(sorted(str_numbers, key=cmp_to_key(compare)))


if __name__ == '__main__':
    print(print_min_number([3, 321, 32]))
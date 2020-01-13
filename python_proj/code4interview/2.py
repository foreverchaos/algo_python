"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


def replace_space(s):
    new_list = list(s)
    for idx, letter in enumerate(new_list):
        if letter == ' ':
            new_list[idx] = '%20'
    return ''.join(new_list)


if __name__ == '__main__':
    print(replace_space('We Are Happy'))
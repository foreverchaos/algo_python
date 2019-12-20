def left_rotate_string(s, n):
    new = [None] * len(s)
    for key, item in enumerate(s):
        new[key-n] = item
    return ''.join(new)


if __name__ == '__main__':
    string = 'abcXYZdef'
    print left_rotate_string(string, 3)
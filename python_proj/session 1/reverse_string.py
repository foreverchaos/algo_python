
def reverse_string(input_str):
    if not isinstance(input_str, str):
        return Exception('not string')
    else:
        new_list = list(input_str)
        i, j = 0, len(new_list) - 1
        while i < j:
            new_list[i], new_list[j] = new_list[j], new_list[i]
            i += 1
            j -= 1
        return ''.join(new_list)


if __name__ == '__main__':
    print(reverse_string('algorithm'))

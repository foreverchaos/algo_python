def find_continuous_seq_for_sun(target):
    windows = []
    for i in range(target):
        windows.append(i)
        while sum(windows) > target:
            windows.pop(0)
            if sum(windows) == target:
                yield windows


if __name__ == '__main__':
    for item in find_continuous_seq_for_sun(100):
        print(item)

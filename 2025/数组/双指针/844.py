def backspaceCompare(s: str, t: str) -> bool:

    def build (s: str) -> str:
        res = []
        for ch in s:
            if ch != '#':
                res.append(ch)
            else:
                if res:
                    res.pop()
        return "".join(res)
    return build(s) == build(t)


if __name__ == '__main__':
    res = backspaceCompare("ab#c", "ad#c")
    print(res)
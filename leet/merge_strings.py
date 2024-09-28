def merge_strings(word1: str, word2: str) -> str:
    merged = []
    i = j = 0
    while i != len(word1) or j != len(word2):
        if i < len(word1):
            merged.append(word1[i])
            i += 1
        if j < len(word2):
            merged.append(word2[j])
            j += 1

    return "".join(merged)


def merge_strings_recur(word1: str, word2: str) -> str:
    res = []
    i = j = 0

    def helper():
        nonlocal i, j
        if i == len(word1) and j == len(word2):
            return
        if i < len(word1):
            res.append(word1[i])
            i += 1
        if j < len(word2):
            res.append(word2[j])
            j += 1
        helper()

    helper()
    return "".join(res)


if __name__ == '__main__':
    print(merge_strings("abcd", "pq"))
    pass

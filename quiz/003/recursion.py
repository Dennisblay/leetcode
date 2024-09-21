def out(num: int):
    if num <= 0:
        return
    print(num, end=' ')
    out(num - 1)
    print(num, end=' ')


def factorial_recursive(num: int) -> int:
    if num <= 1:
        return 1
    return factorial_recursive(num - 1) * num


def factorial_iterative(num: int) -> int:
    if num <= 1:  # not risk a stack overflow error
        return 1

    for i in range(1, num):
        num *= i
    return num


def acc_desc(num: int) -> int:
    if num <= 0:
        return num
    return acc_desc(num - 1) + num


def acc_asc(acc: int, n: int) -> int:
    if acc >= n:
        return acc
    return acc_asc(acc + 1, n) + acc


if __name__ == '__main__':
    # print(acc_desc(4))
    print(acc_asc(0, 4))

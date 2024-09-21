def fibonacci_recursive(num: int) -> int:
    """
    :param num:
    :return:
    the fibonacci sequence up to F(N)
    """
    # Base condition
    # return num if num <= 1 else fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)
    if num <= 0:
        return 0
    elif num == 1:
        return 1

    return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)


def fibonacci_iterative(num: int) -> int:
    if num <= 0:
        return 0
    elif num == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, num + 1):
        a, b = b, a + b

    return b

if __name__ == "__main__":
    for i in range(10):
        print(f"{fibonacci_iterative(i)}[{i}]", end=" -> ")
    print("\n")
    for i in range(10):
        print(f"{fibonacci_recursive(i)}[{i}]", end=" -> ")

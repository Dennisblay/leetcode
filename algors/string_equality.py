def string_equal(str1: str, str2: str) -> bool:
    """
    Compares two strings for equality
    :param str1: string to be compared with
    :param str2: string to compare
    :return: true if both strings are equal
    """
    str1_length = len(str1)
    str2_length = len(str2)
    if str1_length != str2_length:
        return False
    i = 0
    while i < str1_length and str1[i] == str2[i]:
        i = i + 1
    return i == str1_length

if __name__ == '__main__':
    print(string_equal(str1="Hello", str2="World"))
    print(string_equal(str1="Hello", str2="Hello"))

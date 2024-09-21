# Time complexity (T) = # Nodes x work done in each node
# Space complexity (S) = Maximum depth
# T, S = O(N)
def kth_symbol(n: int, k: int) -> int:
    if n == 1:
        return 0
    row_length: int = 2 ** (n - 1)
    mid_index: int = row_length // 2
    if k <= mid_index:
        return kth_symbol(n - 1, k)
    else:
        return 1 - (kth_symbol(n - 1, k - mid_index))
        # return int(not (kth_symbol(n - 1, k - mid_index)))


if __name__ == "__main__":
    print(kth_symbol(4, 5))

# """
#    eg:
#          0            n = 1
#         0 1           n = 2
#       0 1 1 0         n = 3
#   0 1 1 0 1 0 0 1     n = 4
#    :param n:
#    :param k:
#    :return:
#    value 0 or 1 at the kth index
# """

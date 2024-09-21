def toh(N: int, fromm: str, to: str, aux: str) -> int:
    # code below
    # sample print statements below
    # print("move disk " + 1 + " from rod " + 1 + " to rod " + 2)
    # remember to return the number of moves as well

    # ( n - 1 ) disk
    # nth disk
    # (n - 1) disk

    count = 0

    def helper(N: int, fromm: str, to: str, aux: str):
        nonlocal count
        # base case
        if N == 1:
            print("move disk " + str(N) + " from rod " + fromm + " to rod " + to)
            count += 1
            return
        # recursive case
        helper(N - 1, fromm, aux, to)
        print("move disk " + str(N) + " from rod " + fromm + " to rod " + to)
        count += 1
        helper(N - 1, aux, to, fromm)

    helper(N, fromm, to, aux)
    # T = #N x work done per node => O(2^N) - 1 ~ O(2^N)
    # S = #d

    return count  # return the number of moves


if __name__ == '__main__':
    print(f"{toh(3, "A", "C", "B")} movements")

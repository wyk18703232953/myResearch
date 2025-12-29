# Converted version with main(n) and generated test data

import random

def check(mid, arr, m, n):
    ls = [[] for _ in range(1 << m)]
    for i in range(n):
        ans = 0
        for j in range(m):
            if arr[i][j] >= mid:
                ans += 1 << j
        ls[ans].append(i + 1)
    full_mask = (1 << m) - 1
    for i in range(len(ls)):
        if not ls[i]:
            continue
        for j in range(len(ls)):
            if ls[j] and (i | j) == full_mask:
                return ls[i][0], ls[j][0]
    return 0


def solve(arr):
    n = len(arr)
    if n == 0:
        return (1, 1)
    m = len(arr[0]) if arr[0] else 0
    hi, lo, ind1 = 10 ** 9, 0, (1, 1)
    while hi >= lo:
        mid = (hi + lo) // 2
        ind = check(mid, arr, m, n)
        if ind:
            ind1 = ind
            lo = mid + 1
        else:
            hi = mid - 1
    return ind1


def main(n):
    """
    n: problem size, here used as number of rows.
    m is chosen as min(8, max(1, n.bit_length())) to keep 2^m manageable.
    Values are random in [0, 1e9].
    """
    if n <= 0:
        return (1, 1)

    # choose m so that 2^m is not too large, but grows with n
    m = min(8, max(1, n.bit_length()))
    rnd = random.Random(0)
    arr = [[rnd.randint(0, 10**9) for _ in range(m)] for _ in range(n)]
    return solve(arr)


if __name__ == '__main__':
    # example: run main with n = 5
    result = main(5)
    print(*result)
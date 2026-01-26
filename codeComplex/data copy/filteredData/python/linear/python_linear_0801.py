def main(n):
    # Interpret n as the size of arr and set parameters deterministically
    if n <= 0:
        return 0
    m = n
    k = max(1, n // 10)  # ensure k >= 1

    # Generate a deterministic, non-decreasing arr of length m
    # Values are 1-based, increasing with occasional repeats
    arr = [(i * 3) // 2 + 1 for i in range(m)]

    modulo = 0
    tmp = 0
    op = 1
    cur = (arr[0] - 1) // k
    for i in range(m):
        if (arr[i] - 1 - modulo) // k != cur:
            modulo += tmp
            cur = (arr[i] - 1 - modulo) // k
            tmp = 0
            op += 1
        tmp += 1
    return op


if __name__ == "__main__":
    # Example deterministic calls for time-complexity experiments
    for size in [10, 100, 1000]:
        result = main(size)
        # print(size, result)
        pass
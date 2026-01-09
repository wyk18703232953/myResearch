def main(n):
    # Generate deterministic input A based on n
    # Original code expects a list of integers from a single line
    # Here, let A be a sorted list of integers derived from 1..n,
    # mapped into the range [1, 100] to keep behavior meaningful.
    if n <= 0:
        A = []

    else:
        A = [(i % 100) + 1 for i in range(1, n + 1)]
        A.sort()

    B = [0] * 100
    for i in A:
        j = 0
        for c in range(100):
            if B[c] == 0:
                j = c
                break

        while j < 100:
            B[j] = 1
            j += i

    if B.count(0) == 0:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(1000)
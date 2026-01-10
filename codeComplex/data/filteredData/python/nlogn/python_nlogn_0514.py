def main(n):
    from collections import Counter

    # Interpret n as: number of test cases = n,
    # and for each test case, array length = n as well (scales O(n^2) overall).
    t = n

    # Deterministic generation of all test cases
    # For test case i (0-based), generate an array A_i of length n:
    # A[j] = (j % (i+2)) + 1  ensures repetitions and structure vary with i, but are deterministic.
    for case_idx in range(t):
        length = n
        A = [(j % (case_idx + 2)) + 1 for j in range(length)]

        C = Counter(A)
        B = []
        for k, v in C.items():
            if v >= 4:
                B.append(k)
                B.append(k)
            elif v >= 2:
                B.append(k)
        B.sort()
        l = len(B)
        m = 10**18
        ans = [-1, -1, -1, -1]
        for i in range(l - 1):
            x, y = B[i], B[i + 1]
            temp = (4 * (x + y) ** 2) / (x * y)
            if temp < m:
                m = temp
                ans = [x, x, y, y]
        print(*ans)


if __name__ == "__main__":
    main(5)
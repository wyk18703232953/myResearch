def main(n):
    if n < 2:
        print(0)
        return

    k = max(1, n // 3)
    A = [i * 2 + (i % 3) for i in range(n)]

    B = []
    for i in range(n - 1):
        B.append([A[i + 1] - A[i], i])
    B.sort(reverse=True)

    C = []
    for i in range(min(k - 1, len(B))):
        C.append(B[i][1])
    C.sort()

    ans = 0
    mi = 10 ** 9
    ma = -10 ** 9
    u = 0
    for i in range(n):
        mi = min(mi, A[i])
        ma = max(ma, A[i])
        if u < len(C) and i == C[u]:
            ans += ma - mi
            mi = 10 ** 9
            ma = -10 ** 9
            u += 1
    print(ans + ma - mi)


if __name__ == "__main__":
    main(10)
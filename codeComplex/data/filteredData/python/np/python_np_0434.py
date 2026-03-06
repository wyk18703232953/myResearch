def check(mid: int, n: int, m: int, a, ans_holder) -> bool:
    dic = {}
    for i in range(n):
        bit = 0
        for j in range(m):
            if a[i][j] >= mid:
                bit += 1
            bit <<= 1
        dic[bit >> 1] = i
    full = (1 << m) - 1
    for x, idx in dic.items():
        for y, idy in dic.items():
            if x | y == full:
                ans_holder[0] = (idx + 1, idy + 1)
                return True
    return False


def main(n: int):
    # Interpret n as the number of rows; fix m deterministically as a small function of n
    # to keep input size scalable and deterministic.
    if n <= 0:
        return

    m = max(1, min(10, n))  # bounded but grows with n until 10

    # Deterministic generation of matrix a (n x m)
    # Example pattern: a[i][j] = (i * 131 + j * 17) % 1000000000
    a = [[(i * 131 + j * 17) % 1000000000 for j in range(m)] for i in range(n)]

    ans_holder = [(-1, -1)]
    le = 0
    ri = 10**9
    while le <= ri:
        mid = (le + ri) >> 1
        if check(mid, n, m, a, ans_holder):
            le = mid + 1
        else:
            ri = mid - 1

    print(ans_holder[0][0], ans_holder[0][1])


if __name__ == "__main__":
    # Example deterministic call; change n to scale input size
    main(1000)
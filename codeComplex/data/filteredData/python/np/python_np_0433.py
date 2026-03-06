def main(n):
    # Interpret n as matrix size: n x n
    global a, ans, N, M
    N = n
    M = n
    # Deterministic matrix generation: a[i][j] = (i * 131 + j * 37) % 1000
    a = [[(i * 131 + j * 37) % 1000 for j in range(M)] for i in range(N)]
    ans = []

    def check(mid: int) -> bool:
        global ans
        dic = {}
        for i in range(N):
            bit = 0
            for j in range(M):
                if a[i][j] >= mid:
                    bit += 1
                bit <<= 1
            dic[bit >> 1] = i
        full = (1 << M) - 1
        for x, idx in dic.items():
            for y, idy in dic.items():
                if x | y == full:
                    ans = (idx + 1, idy + 1)
                    return True
        return False

    le = 0
    ri = int(1e9)
    while le <= ri:
        mid = (le + ri) >> 1
        if check(mid):
            le = mid + 1
        else:
            ri = mid - 1
    if ans:
        print(ans[0], ans[1])
    else:
        print(-1, -1)


if __name__ == "__main__":
    main(5)
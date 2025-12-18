def main():
    import sys
    read = sys.stdin.read
    readline = sys.stdin.readline
    INF = 1 << 60
    MOD = 10 ** 9 + 7
    sys.setrecursionlimit(10 ** 5)
    """+:-:+:-:+:-:+:-:+:-:+:-:+:-:+:-:+:-:+:-:+:-:+:-:+:-:+:-+:-"""

    def new_dp():
        return [[INF] * M for _ in range(N)]

    def solve():
        if K % 2 == 1:
            for row in range(N):
                print(*[-1] * M)
            return

        dp_prev = [[0] * M for _ in range(N)]

        for _ in range(K // 2):
            dp_cur = new_dp()
            for row in range(N):
                for col in range(M - 1):
                    cost = e1[row][col]
                    dp_cur[row][col] = min(dp_cur[row][col], dp_prev[row][col + 1] + cost)
                    dp_cur[row][col + 1] = min(dp_cur[row][col + 1], dp_prev[row][col] + cost)
            for row in range(N - 1):
                for col in range(M):
                    cost = e2[row][col]
                    dp_cur[row][col] = min(dp_cur[row][col], dp_prev[row + 1][col] + cost)
                    dp_cur[row + 1][col] = min(dp_cur[row + 1][col], dp_prev[row][col] + cost)
            dp_prev = dp_cur

        for row in range(N):
            _r = [2 * x for x in dp_prev[row]]
            print(*_r)

    N, M, K = map(int, readline().split())

    e1 = []
    for _ in range(N):
        r = tuple(map(int, readline().split()))
        e1.append(r)
    e2 = []

    for _ in range(N - 1):
        r = tuple(map(int, readline().split()))
        e2.append(r)
    solve()


if __name__ == '__main__':
    main()

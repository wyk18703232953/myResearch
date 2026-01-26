def main(n):
    from math import inf

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # Map n to N, M, K in a deterministic, scalable way
    if n < 3:
        N = 2
        M = 2
        K = 2

    else:
        N = n
        M = n
        # Ensure K is even and scales with n
        K = 2 * (n // 2)

    # Deterministic generation of wx (N x M) and wy ((N-1) x M)
    wx = [[(i * M + j) % 10 + 1 for j in range(M)] for i in range(N)]
    wy = [[((i + 1) * M + j) % 10 + 1 for j in range(M)] for i in range(N - 1)]

    if K & 1:
        # Same behavior as original: if K is odd, output -1 grid
        for i in range(N):
            for j in range(M):
                # print(-1, end=' ')
                pass
            # print()
            pass
        return

    mem = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K + 1)]

    half = K // 2
    for kk in range(1, half + 1):
        for yy in range(N):
            for xx in range(M):
                mem[kk][yy][xx] = inf

                for d in range(4):
                    y = yy + dy[d]
                    x = xx + dx[d]

                    if y < 0 or y >= N or x < 0 or x >= M:
                        continue

                    if d == 0:
                        mem[kk][yy][xx] = min(
                            mem[kk][yy][xx], mem[kk - 1][y][x] + wx[yy][xx] * 2
                        )
                    elif d == 1:
                        mem[kk][yy][xx] = min(
                            mem[kk][yy][xx], mem[kk - 1][y][x] + wy[yy][xx] * 2
                        )
                    elif d == 2:
                        mem[kk][yy][xx] = min(
                            mem[kk][yy][xx], mem[kk - 1][y][x] + wx[yy][x] * 2
                        )

                    else:
                        mem[kk][yy][xx] = min(
                            mem[kk][yy][xx], mem[kk - 1][y][x] + wy[y][xx] * 2
                        )

    for yy in range(N):
        for xx in range(M):
            # print(mem[half][yy][xx], end=' ')
            pass
        # print()
        pass
if __name__ == "__main__":
    main(5)
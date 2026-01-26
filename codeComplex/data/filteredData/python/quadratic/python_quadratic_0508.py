#!/usr/bin/python3

import math
import sys


DEBUG = False


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        # print(*value, sep=sep, end=end)
        pass


def solve(H, W, A):
    visited = [bytearray(W) for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if A[y][x] == '.' or visited[y][x]:
                continue

            dprint(x, y)
            for dx, dy in [(0, 0), (-1, 0), (-2, 0),
                           (0, -1), (-2, -1),
                           (0, -2), (-1, -2), (-2, -2)]:
                tx = x + dx
                ty = y + dy
                dprint('  ', tx, ty)
                if tx < 0 or ty < 0 or tx + 2 >= W or ty + 2 >= H:
                    continue
                bad = False
                for ex, ey in [(0, 0), (1, 0), (2, 0),
                               (0, 1), (2, 1),
                               (0, 2), (1, 2), (2, 2)]:
                    nx = tx + ex
                    ny = ty + ey
                    if A[ny][nx] == '.':
                        bad = True
                        break
                if bad:
                    continue

                for ex, ey in [(0, 0), (1, 0), (2, 0),
                               (0, 1), (2, 1),
                               (0, 2), (1, 2), (2, 2)]:
                    nx = tx + ex
                    ny = ty + ey
                    visited[ny][nx] = 1

                assert visited[ny][nx] == 1
                break

            if visited[y][x] == 0:
                return False

    return True


def main(n):
    # 映射规模：H = n, W = n
    H = n
    W = n

    # 确定性构造棋盘:
    # 规则：A[y][x] 为 '#' 当且仅当 (x // 3 + y // 3) % 2 == 0；否则为 '.'
    # 这样在 3x3 的块上形成规则图案，规模随 n 线性增长。
    A = []
    for y in range(H):
        row_chars = []
        for x in range(W):
            if ((x // 3) + (y // 3)) % 2 == 0:
                row_chars.append('#')

            else:
                row_chars.append('.')
        A.append(''.join(row_chars))

    result = solve(H, W, A)
    # print('YES' if result else 'NO')
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 以进行规模实验
    main(9)
#!/usr/bin/python3

import random

DEBUG = False


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(H, W, A):
    visited = [bytearray(W) for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if A[y][x] == '.' or visited[y][x]:
                continue

            dprint(x, y)
            for dx, dy in [
                (0, 0), (-1, 0), (-2, 0),
                (0, -1), (-2, -1),
                (0, -2), (-1, -2), (-2, -2)
            ]:
                tx = x + dx
                ty = y + dy
                dprint('  ', tx, ty)
                if tx < 0 or ty < 0 or tx + 2 >= W or ty + 2 >= H:
                    continue
                bad = False
                for ex, ey in [
                    (0, 0), (1, 0), (2, 0),
                    (0, 1), (2, 1),
                    (0, 2), (1, 2), (2, 2)
                ]:
                    nx = tx + ex
                    ny = ty + ey
                    if A[ny][nx] == '.':
                        bad = True
                        break
                if bad:
                    continue

                for ex, ey in [
                    (0, 0), (1, 0), (2, 0),
                    (0, 1), (2, 1),
                    (0, 2), (1, 2), (2, 2)
                ]:
                    nx = tx + ex
                    ny = ty + ey
                    visited[ny][nx] = 1

                assert visited[ny][nx] == 1
                break

            if visited[y][x] == 0:
                return False

    return True


def generate_test_data(n):
    # 把 n 拆成一对 (H, W)，尽量接近正方形
    H = int(n**0.5)
    if H < 1:
        H = 1
    W = max(1, n // H)
    # 若 H*W < n，则补到至少 n 个格子
    while H * W < n:
        W += 1

    # 随机生成由 '#' 和 '.' 组成的 H×W 网格
    # 控制一下密度，让两种符号大致都有
    A = []
    for _ in range(H):
        row = []
        for _ in range(W):
            # 以 50% 概率放 '#'
            cell = '#' if random.random() < 0.5 else '.'
            row.append(cell)
        A.append(''.join(row))

    return H, W, A


def main(n):
    H, W, A = generate_test_data(n)
    # 返回结果，便于在其他地方调用或测试
    return 'YES' if solve(H, W, A) else 'NO'
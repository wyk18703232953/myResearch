#!/bin/python3
from itertools import product

moves = [(x * mx, y * my) for mx, my, (x, y) in product((-1, 1), (-1, 1), ((1, 2), (2, 1)))]

def ac(l, x):
    if l == 0:
        return 0
    return l[x] if 0 <= x < len(l) else 0

def work(a):
    x = 1
    while x:
        x = 0
        for r in range(len(a)):
            for c in range(len(a[0])):
                if not a[r][c] and sum(ac(ac(a, r + dr), c + dc) for dr, dc in moves) >= 4:
                    a[r][c] = 1
                    x = 1

def main(n: int):
    cand = set()

    for i in range(1000):
        for x, y in ((0, i), (i, 0), (i, 1), (-i, 0), (-i, 1), (0, -i)):
            if x == 0 or x % 3 != 1:
                if n == len(cand):
                    break
                cand.add((x, y))
        if len(cand) == n:
            break

    assert len(cand) == n

    for x, y in cand:
        print(x, y)


if __name__ == "__main__":
    # 示例：生成规模为 10 的测试数据
    main(10)
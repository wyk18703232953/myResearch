#!/usr/bin/python3
import random


def solve(N, A):
    cnt = [0] * (N + 1)

    evd = {}
    xs = []
    for a, b in A:
        if a not in evd:
            evd[a] = [0, 0]
            xs.append(a)
        if b not in evd:
            evd[b] = [0, 0]
            xs.append(b)

        evd[a][0] += 1
        evd[b][1] += 1

    xs.sort()

    px = xs[0] - 1
    pop = 0
    for x in xs:
        cnt[pop] += x - px - 1
        cnt[pop + evd[x][0]] += 1
        pop -= evd[x][1]
        pop += evd[x][0]
        px = x

    return cnt[1:]


def main(n):
    # 生成规模为 n 的测试数据
    N = n
    A = []
    # 生成区间端点，保证 a <= b
    for _ in range(N):
        a = random.randint(1, 10 * n)
        b = random.randint(1, 10 * n)
        if a > b:
            a, b = b, a
        A.append((a, b))

    ans = solve(N, A)
    print(*ans)


if __name__ == '__main__':
    # 示例：以 n=5 运行
    main(5)
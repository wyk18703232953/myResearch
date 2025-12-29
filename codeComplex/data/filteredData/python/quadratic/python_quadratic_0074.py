from math import factorial
from random import randint


def nCr(n, r):
    f, m = factorial, 1
    for i in range(n, n - r, -1):
        m *= i
    return int(m // f(r))


def main(n):
    # 生成长度为 n 的随机数组 a，元素范围 1..n
    a = [randint(1, n) for _ in range(n)]

    # 生成随机查询数量 q，范围 1..n
    q = randint(1, n)
    queries = []
    for _ in range(q):
        l = randint(1, n)
        r = randint(l, n)  # 保证 l <= r
        queries.append((l, r))

    # 原始逻辑开始
    ans, tem = [], 0
    mem = [0] * (n + 1)

    for i in range(n):
        for j in range(a[i] - 1, 0, -1):
            if not mem[j]:
                tem += 1
        mem[a[i]] = 1

    for l, r in queries:
        tem += nCr(r - l + 1, 2)
        ans.append('odd' if tem % 2 else 'even')

    print('\n'.join(ans))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
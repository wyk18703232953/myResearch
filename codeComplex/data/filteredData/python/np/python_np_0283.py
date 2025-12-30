from math import log
import random

mod = 1000000007
inf = float("inf")
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def bo(i):
    return ord(i) - ord('a')


def solve(n, queries):
    """
    n: size parameter (integer)
    queries: list of (u, s) pairs
    """
    x = int(log(n + 1, 2))
    root = 1 << (x - 1)

    for u, s in queries:
        pos = 'U'
        if u < root:
            pos = 'L'
        if u > root:
            pos = 'R'

        s1 = bin(u)[2:]
        s1 = '0' * (x - len(s1)) + s1
        s1 = list(s1)

        for j in s:
            for k in range(x - 1, -1, -1):
                if s1[k] == '1':
                    f = k
                    break
            if j == 'L':
                if f == x - 1:
                    continue
                s1[f] = '0'
                s1[f + 1] = '1'
            elif j == 'R':
                if f == x - 1:
                    continue
                s1[f + 1] = '1'
            else:
                if f == 0:
                    continue
                if s1[f - 1] == '1':
                    s1[f] = '0'
                else:
                    s1[f - 1] = '1'
                    s1[f] = '0'

        s1 = "".join(s1)
        print(int(s1, 2))


def main(n):
    """
    n: 规模参数，用来生成测试数据。
       要求原程序中 2^(x-1) <= n < 2^x，使得 log(n+1,2) 的行为合理。
       推荐 n 为 2^k - 1 形式，例如 7, 15, 31 等。
    测试数据生成策略：
      - q = max(1, min(n, 10)) 条查询
      - 每个 u 为 [1, n] 间随机数
      - 每个 s 为长度 [0, x] 的随机字符串，字符来自 'L','R','U'
    """
    # 保证 n 合法（至少为 1）
    if n < 1:
        n = 1

    x = int(log(n + 1, 2))

    # 生成 q 条查询
    q = max(1, min(n, 10))
    letters = ['L', 'R', 'U']
    queries = []
    for _ in range(q):
        u = random.randint(1, n)
        length = random.randint(0, x)  # 操作序列长度
        s = ''.join(random.choice(letters) for _ in range(length))
        queries.append((u, s))

    solve(n, queries)


if __name__ == "__main__":
    # 示例：以 n = 15 运行
    main(15)
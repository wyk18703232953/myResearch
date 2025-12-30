from os import path
import sys

mod = 1000000007
inf = float("inf")
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def ceil(a, b):
    return (a + b - 1) // b


def solve(l, r):
    s1 = bin(l)[2:]
    s2 = bin(r)[2:]
    if len(s1) != len(s2):
        return (1 << len(s2)) - 1

    x = 0
    for i in range(62, -1, -1):
        if ((l >> i) & 1) ^ ((r >> i) & 1):
            x += (1 << (i + 1))
            x -= 1
            break
    return x


def main(n):
    """
    生成规模为 n 的测试数据并执行算法。
    这里将生成 n 对 (l, r)：
    第 i 对为 (i, 2*i + 1)，保证 l <= r 且有一定变化。
    返回所有结果组成的列表。
    """
    res = []
    for i in range(1, n + 1):
        l = i
        r = 2 * i + 1
        res.append(solve(l, r))
    return res


if __name__ == "__main__":
    # 示例：运行 main(5) 并打印结果
    ans = main(5)
    for v in ans:
        print(v)
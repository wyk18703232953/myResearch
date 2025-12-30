from os import path
import sys
from random import randint

mod = 1000000007
inf = float("inf")

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
    # 根据 n 生成测试数据，这里生成 n 组 (l, r)，并输出对应答案
    # 约束：0 <= l <= r <= 10^18
    MAXV = 10**18
    results = []
    for _ in range(n):
        l = randint(0, MAXV)
        r = randint(l, MAXV)  # 保证 l <= r
        ans = solve(l, r)
        results.append(str(ans))
    print("\n".join(results))

if __name__ == "__main__":
    # 默认测试规模可以自行调整
    main(5)
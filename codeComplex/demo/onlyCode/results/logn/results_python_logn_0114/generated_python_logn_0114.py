#!/usr/bin/env python
import random

def solve(l, r):
    n = len(bin(r)[2:])
    ans = 0
    for x in range(0, n + 1):
        if (r >> x) & 1 == 1 and (l >> x) & 1 == 0:
            ans = max(ans, (1 << x) ^ ((1 << x) - 1))
    return ans

def main(n):
    # 根据规模 n 生成测试数据：
    # 令 r 在 [1, 2^n - 1] 内随机，l 在 [0, r] 内随机
    if n <= 0:
        n = 1
    max_val = (1 << n) - 1
    r = random.randint(1, max_val)
    l = random.randint(0, r)
    ans = solve(l, r)
    print(ans)

if __name__ == "__main__":
    # 示例：可自行修改 n 测试
    main(10)
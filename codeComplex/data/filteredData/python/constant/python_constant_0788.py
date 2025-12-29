import math
import random

def solve(n):
    if not n % 2 and math.isqrt(n // 2) ** 2 == n // 2:
        print('YES')
        return
    if not n % 4 and math.isqrt(n // 4) ** 2 == n // 4:
        print('YES')
        return
    print('NO')

def main(t):
    # 生成 t 个测试数据并调用 solve
    random.seed(0)
    for _ in range(t):
        # 这里生成 [1, 10^9] 范围内的随机整数作为 n
        n = random.randint(1, 10**9)
        solve(n)

if __name__ == "__main__":
    # 示例：运行规模 t=5
    main(5)
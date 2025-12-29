import math
import random

def main(n):
    # 生成测试数据：
    # 令 x 在 [0, 10^9] 之间，k 在 [0, n] 之间
    x = random.randint(0, 10**9)
    k = random.randint(0, n)

    mod = 10**9 + 7
    if x > 0:
        ans = (pow(2, k + 1, mod) * x - pow(2, k, mod) + 1) % mod
    else:
        ans = 0

    print(ans)

if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)
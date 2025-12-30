from math import *
from fractions import *
import random

def main(n):
    # 生成测试数据：k 在 [1, n] 范围内随机取值
    if n <= 0:
        return
    k = random.randint(1, n)

    # 原逻辑开始
    if k == 1:
        ans = "1" + "0" * (n - 1)
    else:
        a = (n - k) // 2
        p = "1" + "0" * a
        ans = p * (n // (a + 1)) + p[:(n % (a + 1))]
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
import math
import random

def main(n):
    # 生成测试数据：
    # n 固定为传入规模
    # 约束：m, k, l 为不超过 n 的正整数
    if n <= 0:
        raise ValueError("n must be positive")

    m = random.randint(1, n)
    k = random.randint(0, n)
    l = random.randint(0, n)

    # 原逻辑开始
    x = (l + k) // m
    if x * m < l + k:
        x += 1
    assert x * m >= l + k

    if m * x > n:
        print(-1)
    else:
        print(x)

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(100)
import math
import random

def main(n):
    # 生成测试数据：
    # 让 k 也随规模 n 变化，这里简单设定 k 为 1..n 之间的随机数
    if n <= 1:
        # 保证有意义的范围
        n = 2
    k = random.randint(1, n)

    # 原逻辑开始
    N = n
    K = k
    N -= 1
    K -= 1

    if N > (K * (K + 1)) // 2:
        print(-1)
        return

    l = -1
    r = K + 1
    while r > l + 1:
        m = (l + r) // 2
        if N > (m * (2 * K - m + 1)) // 2:
            l = m
        else:
            r = m
    print(r)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
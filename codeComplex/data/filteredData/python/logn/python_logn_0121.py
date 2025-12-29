import math
import random

def main(n):
    # 生成测试数据：给定规模 n，构造 n 和 k
    # 这里示例设定：n 为题目中的 n，k 取 1 到 n 之间的随机值
    if n < 1:
        return
    k = random.randint(1, n)

    # 原逻辑开始
    n_val = n - 1
    k_val = k - 1
    if n_val > (k_val * (k_val + 1)) // 2:
        print(-1)
    else:
        l = -1
        r = k_val + 1
        while r > l + 1:
            m = (l + r) // 2
            if n_val > (m * (2 * k_val - m + 1)) // 2:
                l = m
            else:
                r = m
        print(r)

# 示例调用
if __name__ == "__main__":
    main(10)
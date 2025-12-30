from collections import Counter
import random

def main(n: int):
    # 生成测试数据：
    # 随机生成一个合法的 p，使得存在对应的 k
    # 原式：p*(p+1)//2 - (n-p) = k
    # 对给定 n, p，直接计算 k 即可
    if n < 0:
        raise ValueError("n must be non-negative")

    # 在 [0, n] 中随机选择一个 p，用于生成一组 (n, k)
    p_true = random.randint(0, n)
    k = p_true * (p_true + 1) // 2 - (n - p_true)

    # 原始逻辑：已知 n, k，枚举 p，找到满足条件的 n-p 并输出
    for p in range(n + 1):
        if p * (p + 1) // 2 - (n - p) == k:
            print(n - p)
            break

if __name__ == "__main__":
    # 示例：可在此处修改测试规模
    main(10)
#!/usr/bin/env python3
import random

def main(n: int):
    """
    n: 作为规模参数，用于生成测试数据。
       这里假设 n 是原程序中的 n 的上界，用来构造合理的 (n, m, k, l)。
    """
    # 随机生成测试数据（仅示例策略，可按需要调整）：
    # 1. 随机选择真实的 n_val ∈ [1, n]
    # 2. m ∈ [1, n_val]
    # 3. k, l ∈ [0, n_val]（允许 0 是为了覆盖边界）
    if n <= 0:
        raise ValueError("n must be positive as a scale parameter.")

    n_val = random.randint(1, n)
    m = random.randint(1, max(1, n_val))       # 保证 m ≥ 1
    k = random.randint(0, n_val)
    l = random.randint(0, n_val)

    # 原始逻辑
    q = (l + k - 1) // m + 1
    if q * m > n_val:
        result = -1
    else:
        result = q

    # 输出结果（只打印最终答案；如果需要也可打印生成的数据）
    print(result)

if __name__ == "__main__":
    # 示例：以 10 为规模调用 main，可按需要修改或在外部调用 main
    main(10)
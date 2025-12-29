import math
import random

def solve_single(n, k):
    limit = -1
    if n <= 60:
        limit = 0
        pow4 = 1
        for _ in range(n):
            limit += pow4
            pow4 *= 4
    if (limit < k and limit != -1) or (n == 2 and k == 3):
        return 'NO'
    else:
        div = 1
        k -= 1
        size = 1
        while div < n and k >= 4 * size - 1:
            k -= 4 * size - 1
            size *= 2
            div += 1
        return 'YES ' + str(n - div)

def main(n):
    # n 作为规模参数，用来生成测试数据：
    # 生成 t 个测试用例，t 与 n 同数量级
    t = max(1, n)  # 至少一个测试
    results = []
    for _ in range(t):
        # 生成每个测试的 n_i, k_i
        # 让 n_i 在 [1, n] 范围，k_i 在 [1, 4^min(n_i,10)] 范围内，避免过大整数
        ni = random.randint(1, n)
        max_pow_exp = min(ni, 10)
        max_k = (4 ** max_pow_exp - 1) // 3  # 1 + 4 + 4^2 + ... + 4^(exp-1)
        ki = random.randint(1, max_k if max_k > 0 else 1)
        results.append(solve_single(ni, ki))
    print("\n".join(results))

if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)
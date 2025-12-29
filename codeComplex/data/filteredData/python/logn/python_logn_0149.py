import random

def main(n):
    # 生成测试数据：随机选择 k，且保证 n <= k*(k+1)//2
    # 这里将 k 规模设为与 n 同数量级
    if n <= 0:
        print(-1)
        return

    # 为了保证存在可行解，先选 k 使得 k*(k+1)//2 >= n
    k = max(1, int((2 * n) ** 0.5))  # 近似满足 k*(k+1)//2 ≈ n
    while k * (k + 1) // 2 < n:
        k += 1

    # 可以稍微随机扰动 k（不影响规模量级）
    k += random.randint(0, n // 10 + 1)

    # 原逻辑开始
    n, k = n - 1, k - 1
    l = 0
    r = k
    g = k * (k + 1) // 2
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if (g - m * (m + 1) // 2) >= n:
            ans = k - m
            l = m + 1
        else:
            r = m - 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)
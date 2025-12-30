import random

def main(n: int) -> None:
    # 生成测试数据：
    # n: 数组长度
    # m: 窗口大小 (1 <= m <= n)
    # k: 惩罚值 (整数，可正可负)
    m = random.randint(1, max(1, n))
    # 这里让 k 在一个相对适中的范围内，便于测试
    k = random.randint(-10, 10)
    # 生成数组 a，元素范围可按需调整
    a = [random.randint(-10, 10) for _ in range(n)]

    dp = [-1] * (n + 15)
    for i in range(n):
        s = a[i]
        mx = max(0, a[i])
        # j 从 i-1 递减到 max(-1, i-m) + 1
        for j in range(i - 1, max(-1, i - m), -1):
            s += a[j]
            mx = max(mx, s)
        dp[i] = max(0, (dp[i - m] + s - k) if i - m >= 0 else -10**18, mx - k)
    print(max(dp))


# 示例：直接运行时用一个默认规模
if __name__ == "__main__":
    main(10)
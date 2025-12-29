import random

def main(n):
    # 生成测试数据：
    # a 长度为 n
    # b 长度为 m，且 m >= n（否则原算法中的区间会越界）
    m = 2 * n if n > 0 else 0  # 可根据需要调整规模关系
    a = [random.randint(0, 1) for _ in range(n)]
    b = [random.randint(0, 1) for _ in range(m)]

    # 原始逻辑开始
    ans = 0
    for i in range(n):
        ans += a[i] ^ b[i]

    ones = [0 for _ in range(m)]
    zeros = [0 for _ in range(m)]

    for i in range(m):
        if b[i]:
            ones[i] = 1
        else:
            zeros[i] = 1

    for i in range(1, m):
        ones[i] += ones[i - 1]
        zeros[i] += zeros[i - 1]

    for i in range(n):
        if a[i] == 1:
            ans += zeros[m - n + i] - zeros[i]
        else:
            ans += ones[m - n + i] - ones[i]

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
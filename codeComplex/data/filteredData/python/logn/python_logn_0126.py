import random

def main(n):
    # 生成测试数据：根据规模 n 生成一个合适的 k
    # 这里简单设定 k 在 [1, max(2, 2*n)] 区间内随机取值
    if n <= 0:
        raise ValueError("n must be positive")
    k = random.randint(1, max(2, 2 * n))

    # 原逻辑开始
    if n == 1:
        ans = 0
    elif k + (k - 1) * (k - 2) // 2 < n:
        ans = -1
    else:
        l = 0
        r = k - 1
        while r - l > 1:
            m = (l + r) // 2
            if (2 * k - m + 1) * m // 2 - (m - 1) >= n:
                r = m
            else:
                l = m
        ans = r

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行修改
    main(10)
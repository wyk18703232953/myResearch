import random

def main(n: int):
    # 预设最大坐标范围，与原程序一致
    MAXN = 1000007

    # 生成测试数据：
    # n 对 (a, b)，其中：
    #   1 <= a < MAXN-5，b >= 0，且 a - b - 1 >= 0（保证 dp 访问合法）
    # 保证 a 不越界、访问 dp[i - b - 1] 时不为负。
    pairs = []
    for _ in range(n):
        # a 至少为 1，这样 i - b - 1 最低为 0
        a = random.randint(1, MAXN - 5)
        # 让 b 不超过 a-1 确保 i-b-1 >= 0
        b = random.randint(0, a - 1)
        pairs.append((a, b))

    # 以下为原逻辑改写，无 input()
    dp = [0] * MAXN
    majak = [0] * MAXN

    q = MAXN
    for a, b in pairs:
        q = min(q, a)
        majak[a] = b

    # 如果 n=0 或生成的数据导致 q 未被更新，则直接输出 n
    if q == MAXN:
        print(n)
        return

    dp[q] = 1
    ma = 1

    # 原代码循环上界为 1000003
    for i in range(q + 1, 1000003):
        if majak[i] == 0:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - majak[i] - 1] + 1
            if dp[i] > ma:
                ma = dp[i]

    print(n - ma)


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n
    main(10)
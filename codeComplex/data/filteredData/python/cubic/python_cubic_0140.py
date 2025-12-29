from math import inf
import random

def solve(a):
    n = len(a) - 1  # a is 1-indexed with dummy at index 0
    dp = [[[-1, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    # dp[i][j] = [value, can_reduce_to_len1]

    for i in range(1, n + 1):
        dp[i][i][0], dp[i][i][1] = a[i], 1

    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n + 1):
            for k in range(j - i):
                left_seg = dp[i][i + k]
                right_seg = dp[i + k + 1][j]
                if left_seg[1] and right_seg[1] and left_seg[0] == right_seg[0]:
                    dp[i][j][0], dp[i][j][1] = left_seg[0] + 1, 1
                    break

    val = [0, 0] + [inf] * n
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j][1]:
                val[j + 1] = min(val[j + 1], val[i] + 1)
    return val[-1]

def main(n):
    # 生成测试数据：长度为 n 的随机数组，元素在 1..3 范围内
    # 可根据需要调整数据生成策略
    a = [0] + [random.randint(1, 3) for _ in range(n)]
    ans = solve(a)
    print(ans)

if __name__ == '__main__':
    # 示例：可以在这里指定 n 进行本地测试
    main(10)
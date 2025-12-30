import random
import math

def count(x):
    ans = 0
    while x:
        x &= x - 1
        ans += 1
    return ans

def main(n):
    # 生成 n×n 的测试数据矩阵 a，a[i][j] 为 [0,1] 之间的随机概率
    # 可根据需要调整测试数据生成方式
    a = [[random.random() for _ in range(n)] for _ in range(n)]

    y = 1 << n
    dp = [0.0] * (y - 1) + [1.0]
    powe = [1 << i for i in range(n)]

    for i in range(y - 1, 0, -1):
        bit = count(i)
        prob = bit * (bit - 1) // 2
        if prob == 0:
            continue
        cur = dp[i]
        if cur == 0:
            continue
        for j in range(n):
            if not (i & powe[j]):
                continue
            for x in range(n):
                if not (i & powe[x]):
                    continue
                dp[i - powe[x]] += cur * a[j][x] * prob
                dp[i - powe[j]] += cur * a[x][j] * prob

    z = sum(dp[1 << i] for i in range(n))
    if z == 0:
        # 避免除零：若 z 为 0，则输出全 0
        result = [0.0 for _ in range(n)]
    else:
        result = [dp[1 << i] / z for i in range(n)]

    # 输出结果
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    # 示例：调用 main(3)，可根据需要修改 n
    main(3)
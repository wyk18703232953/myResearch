from collections import Counter
import random

def main(n, seed=0):
    random.seed(seed)

    # 生成测试数据
    # n: 元素数量
    # k: 每个喜欢的颜色最多可选数量，设为 1~n 之间
    k = random.randint(1, max(1, n))

    # 颜色编号范围和喜欢颜色范围都设为 1..n
    c = [random.randint(1, n) for _ in range(n)]  # 所有物品的颜色
    f = [random.randint(1, n) for _ in range(n)]  # 喜欢的颜色序列

    # h 数组长度为 k+1，h[0] = 0，h[1..k] 随机生成
    h = [0] + [random.randint(0, 10) for _ in range(k)]

    # 原逻辑
    cnt_all = Counter(c)
    cnt_fav = Counter(f)

    ans = 0
    for fi in cnt_fav:
        if fi not in cnt_all:
            continue
        m = cnt_fav[fi]
        t = min(cnt_all[fi], m * k)
        dp = [[0] * (t + 1) for _ in range(m + 1)]
        for x in range(1, m + 1):
            for s in range(0, t + 1):
                for ki in range(0, k + 1):
                    if ki + s > t:
                        break
                    dp[x][ki + s] = max(dp[x][ki + s], dp[x - 1][s] + h[ki])
        ans += dp[m][t]

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)
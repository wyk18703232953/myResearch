import random

def main(n: int):
    # 生成测试数据
    # n: 物品数量
    # k: 每组最大可选数量，设为 1~n 范围内的一个值
    k = max(1, n // 3)
    # 颜色数量与喜欢颜色种类数量控制在 O(n) 内
    max_color = max(1, n // 2)
    max_f = max(1, n // 2)

    # c: 每个物品的颜色，取值范围 [1, max_color]
    c = [random.randint(1, max_color) for _ in range(n)]
    # f: 每个物品喜欢的颜色，取值范围 [1, max_f]
    f = [random.randint(1, max_f) for _ in range(n)]
    # h: 奖励数组，长度为 k，h[i] 为选 i+1 个时的收益
    h = [random.randint(1, 10) for _ in range(k)]

    # 以下为原 solve() 逻辑，移除 input，使用上面生成的数据
    cnt = {}
    for color in c:
        cnt[color] = cnt.get(color, 0) + 1

    likecolor = {}
    for i in range(n):
        likecolor.setdefault(f[i], []).append(i)
        cnt[f[i]] = cnt.get(f[i], 0)

    ans = 0
    for key, v in likecolor.items():
        n1 = len(v)
        if cnt[key] >= n1 * k:
            ans += n1 * h[k - 1]
            continue

        # 注意原代码这里写的是 -float("INF")，会导致 ValueError
        # 按原意应为负无穷
        NEG_INF = float("-inf")
        dp = [[NEG_INF] * (cnt[key] + 1) for _ in range(n1 + 1)]
        dp[0][0] = 0

        for i in range(n1):
            j = i + 1
            for e in range(cnt[key] + 1):
                # 不选第 j 个
                if dp[i][e] > dp[j][e]:
                    dp[j][e] = dp[i][e]
                # 选第 j 个，增加 w-e-1 个，最多 k 个
                upper = min(cnt[key] + 1, e + k + 1)
                for w in range(e + 1, upper):
                    val = dp[i][e] + h[w - e - 1]
                    if val > dp[j][w]:
                        dp[j][w] = val

        ans += dp[n1][cnt[key]]

    print(ans)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)
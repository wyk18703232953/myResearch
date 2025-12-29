from collections import defaultdict
import random

def main(n):
    # 生成测试数据
    # n: 规模，对应原代码中的 n
    # k: 取一个与 n 相关的合理值，避免爆炸式复杂度
    # 这里示例设为 min(10, n)（可根据需要调整）
    k = max(1, min(10, n))

    # c, f 长度为 n，值域在 [1, m]，m 也与 n 相关
    m = max(1, min(10, n))  # 种类数
    c = [random.randint(1, m) for _ in range(n)]
    f = [random.randint(1, m) for _ in range(n)]

    # h 长度为 k+1，索引 0..k
    # 保证非负且不过大
    h = [0] + [random.randint(0, 10) for _ in range(k)]

    # 以下为原逻辑
    cnt1 = defaultdict(lambda: 0)
    for x in c:
        cnt1[x] += 1

    cnt2 = defaultdict(lambda: 0)
    for x in f:
        cnt2[x] += 1

    ans = 0
    for key in cnt2:
        c1, c2 = cnt1[key], cnt2[key]
        dp0 = [0]
        l = 1
        for _ in range(c2):
            dp = [0] * (l + k)
            for i in range(l):
                dp0i = dp0[i]
                for j in range(k + 1):
                    dp[i + j] = max(dp[i + j], dp0i + h[j])
            l += k
            dp0 = dp
        ans += dp[min(c1, k * c2)]

    print(ans)


if __name__ == "__main__":
    # 示例调用
    main(10)
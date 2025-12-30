from collections import Counter, defaultdict
from math import factorial


def comb(n, m):  # 保留原工具函数（未使用）
    return factorial(n) / (factorial(m) * factorial(n - m)) if n >= m else 0


def perm(n, m):  # 保留原工具函数（未使用）
    return factorial(n) // factorial(n - m) if n >= m else 0


def mdis(x1, y1, x2, y2):  # 保留原工具函数（未使用）
    return abs(x1 - x2) + abs(y1 - y2)


def main(n: int):
    """
    参数 n：规模参数，用于生成测试数据。
    这里约定：
        - cds 长度 = n
        - fn 长度  = n // 2  (至少为 1)
        - k        = min(5, n)（奖励数组长度为 k+1）
    测试数据生成规则可以按需修改。
    """

    # ---------------- 生成测试数据 ----------------
    # 为了让不同数据都能覆盖逻辑，生成可重复的 cds 和 fn
    if n <= 0:
        print(0)
        return

    k = min(5, n)

    # cds: 长度 n，数值从 1 到 n//2 循环
    cds = [(i % max(1, n // 2)) + 1 for i in range(n)]

    # fn: 长度 n//2（至少 1），从 1 开始循环
    len_fn = max(1, n // 2)
    fn = [(i % max(1, n // 2)) + 1 for i in range(len_fn)]

    # sc: 长度 k+1，sc[0] = 0, sc[l] = l * 2 之类的简单递增收益
    sc = [0] + [2 * i for i in range(1, k + 1)]

    # ---------------- 原主要逻辑 ----------------
    rec = set(fn)
    uses = 0
    dic = defaultdict(int)
    for x in cds:
        if x in rec:
            dic[x] += 1
            uses += 1

    dp = [[0] * (uses + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, uses + 1):
            for l in range(k + 1):
                if l > j:
                    break
                val = sc[l]
                dp[i][j] = max(dp[i][j], dp[i - 1][j - l] + val)

    res = 0
    for key, v in Counter(fn).items():
        res += dp[v][dic[key]]

    print(res)


if __name__ == "__main__":
    # 示例：用 n=10 运行
    main(10)
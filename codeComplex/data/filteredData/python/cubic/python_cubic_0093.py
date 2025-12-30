import random
from collections import Counter, defaultdict

mod = 998244353
INF = float('inf')


def main(n: int):
    """
    将原逻辑封装为 main(n)：
    - n 为规模参数，这里用作 fn 的最大可能值以及 cds / fn / sc 的长度控制基础。
    - 生成一组自洽的随机数据，并在其上运行原算法。
    """

    # ---------- 1. 生成测试数据 ----------
    # 这里给出一个合理的生成方式，可以按需要自行调整

    # n: 种类数量上限（原 dp 里也是维度之一）
    # k: 每种 cd 的最大可用次数上限
    k = max(1, n // 3)          # k 与 n 同量级
    m_cds = n * k               # cds 的长度
    m_fn = n                    # fn 的长度 (= n 种需求)
    max_sc_len = k              # sc 需要有 k+1 个元素 (0..k)

    # 1) fn: 需求列表（长度 m_fn，每个值在 [1, n]）
    fn = [random.randint(1, n) for _ in range(m_fn)]

    # 2) cds: 可用 cd 列表（长度 m_cds，每个值在 [1, n]）
    cds = [random.randint(1, n) for _ in range(m_cds)]

    # 3) sc: 奖励数组，长度为 k+1，sc[0] = 0
    sc = [0]
    # 设定奖励为非降、随机增量，保证更大使用数量不会更差
    current = 0
    for _ in range(1, max_sc_len + 1):
        current += random.randint(0, 10)
        sc.append(current)

    # ---------- 2. 原始逻辑 ----------

    rec = set(fn)
    uses = 0
    dic = defaultdict(int)
    for x in cds:
        if x in rec:
            dic[x] += 1
            uses += 1

    # dp[i][j]: 在考虑前 i 个 "同一种类" 时，总使用次数为 j 时的最大评分
    # 注意：这里 i 的含义在原题中实际对应于「某种 cd 类型的最大可用次数上限」
    # 但原代码直接用 n, k，因此照抄
    dp = [[0] * (n * k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n * k + 1):
            # 枚举在第 i 个上使用的数量 l
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
    # 示例：以 n = 10 运行一次
    main(10)
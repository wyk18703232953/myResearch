from math import sqrt, ceil
from collections import Counter, defaultdict
from bisect import insort
import random

# 预处理：最小质因子表
MAX_N = 10 ** 7 + 1
spf = [i for i in range(MAX_N)]

for i in range(4, MAX_N, 2):
    spf[i] = 2

for i in range(3, ceil(sqrt(MAX_N))):
    if spf[i] == i:
        step = i
        start = i * i
        for j in range(start, MAX_N, step):
            if spf[j] == j:
                spf[j] = i


def f(x: int) -> int:
    """将 x 变为其平方因子约简后的形式（保留所有质因子奇数次的乘积）"""
    c = Counter()
    ans = 1
    while x != 1:
        p = spf[x]
        c[p] += 1
        x //= p
    for p, cnt in c.items():
        if cnt % 2 == 1:
            ans *= p
    return ans


def solve_single_case(n: int, k: int, a: list[int]) -> int:
    # 将数组元素做平方因子约简
    for i in range(n):
        a[i] = f(a[i])

    # dp_depth[i][x]: 从位置 i 开始，允许至多 x 个“重复元素”（需要改变的元素），
    #                能走到的最远端点索引（end，区间为 [i, end)）
    dp_depth = [[n for _ in range(k + 1)] for _ in range(n)]
    recent = [n for _ in range(k + 1)]  # 存储 suffix 中最近的重复元素位置
    closest = defaultdict(lambda: -1)   # 记录每个值第一次出现的索引

    # 从右往左更新 dp_depth 和 recent
    for i in range(n - 1, -1, -1):
        if closest[a[i]] >= 0:
            insort(recent, closest[a[i]])
            recent.pop()  # 保持 recent 长度为 k+1
        dp_depth[i] = recent.copy()
        closest[a[i]] = i

    # dp[i][x]: 前 i 个元素（[0, i)）在最多 x 次“修改”下最少分成多少段
    dp = [[i for _ in range(k + 1)] for i in range(n + 1)]
    dp[0] = [0 for _ in range(k + 1)]

    for i in range(n):
        for x in range(k + 1):
            end = dp_depth[i][x]
            # 前缀使用 y 次修改，后缀使用 x 次修改，整体不超过 k
            max_y = k - x
            base = dp[i]  # 减少索引开销
            target = dp[end]
            for y in range(max_y + 1):
                new_sets = base[y] + 1
                if new_sets < target[x + y]:
                    target[x + y] = new_sets

    return dp[n][k]


def main(n: int):
    """
    参数:
        n: 数组规模
    行为:
        - 生成一组随机测试数据:
          * k 在 [0, min(20, n)] 范围内
          * 数组 a[i] 在 [1, 10^7] 范围内
        - 执行原逻辑并打印答案
    """
    if n <= 0:
        print(0)
        return

    k = random.randint(0, min(20, n))
    a = [random.randint(1, 10 ** 7) for _ in range(n)]
    ans = solve_single_case(n, k, a)
    print(ans)


# 示例: 手动调用 main
if __name__ == "__main__":
    # 可根据需要修改 n 测试规模
    main(1000)
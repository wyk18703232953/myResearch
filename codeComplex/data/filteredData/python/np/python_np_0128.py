import math
from collections import defaultdict
import random

mod = int(1e9) + 7
INF = float('inf')


def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里生成：
    #   l: n 个 1..50 的随机整数
    #   c: n 个 1..100 的随机整数作为代价
    random.seed(0)  # 为了可复现，可根据需要移除
    l = [random.randint(1, 50) for _ in range(n)]
    c = [random.randint(1, 100) for _ in range(n)]

    d = dict()
    for i in range(n):
        if l[i] in d:
            d[l[i]] = min(d[l[i]], c[i])
        else:
            d[l[i]] = c[i]

    # 注意：原代码在循环内每次都重新生成 lis = list(d.keys())
    # 且在内层使用 d[i]、d[j]，与动态更新交织，保持原逻辑不变
    for i in l:
        lis = list(d.keys())
        for j in lis:
            g = math.gcd(i, j)
            if g in d:
                d[g] = min(d[g], d[i] + d[j])
            else:
                d[g] = d[i] + d[j]

    if 1 in d:
        print(d[1])
    else:
        print(-1)


if __name__ == "__main__":
    # 示例调用：n = 5
    main(5)
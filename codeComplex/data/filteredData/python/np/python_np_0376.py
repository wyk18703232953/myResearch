from math import factorial
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush
import random

INF = float('inf')
mod = 998244353


def cord(c):
    return ord(c) - ord('a')


def main(n):
    """
    将原始基于输入的程序改为：
    - 由参数 n 控制规模
    - 自动生成测试数据
    - 不使用 input()
    这里约定：
    - m 为不同字符种类数，1 <= m <= min(20, n)
    - 字符串 s 长度为 n，由前 m 个小写字母随机生成
    """
    # 根据 n 设定 m（字母表大小）
    m = min(20, max(1, n if n <= 5 else n // 5))

    # 生成长度为 n 的随机字符串，仅用前 m 个小写字母
    letters = [chr(ord('a') + i) for i in range(m)]
    s = ''.join(random.choice(letters) for _ in range(n))

    # 以下为原始逻辑，只是用上述生成的数据替代 input()
    ct = [0] * (1 << m)

    for i in range(n - 1):
        now, nex = cord(s[i]), cord(s[i + 1])
        if now == nex:
            continue
        ct[(1 << now) | (1 << nex)] += 1

    # 子集和 DP：ct[mask] = 所有子集子mask 的累加
    for i in range(m):
        for j in range(1 << m):
            if (1 << i) & j:
                ct[j] += ct[(1 << i) ^ j]

    dp = [INF] * (1 << m)
    dp[0] = 0
    full_mask = (1 << m) - 1

    # 原代码的 ct[-1] = ct[full_mask]
    # ct[~i] 对应的 mask 需要限制到 m 位：mask = (~i) & full_mask
    for i in range(1 << m):
        for j in range(m):
            if (i & (1 << j)) == 0:
                sm = ct[full_mask] - ct[i] - ct[(~i) & full_mask]
                nxt = i | (1 << j)
                if dp[nxt] > dp[i] + sm:
                    dp[nxt] = dp[i] + sm

    # 输出结果，模拟原程序行为
    print(dp[full_mask])


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)
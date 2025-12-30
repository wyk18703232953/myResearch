from collections import defaultdict
from math import gcd
from heapq import heappop, heappush
import random


def main(n: int):
    """
    n: problem scale, also the length of arrays A, B to be generated.
    This function:
    - Generates random test data A, B of length n
    - Runs the original algorithm logic
    - Prints the answer
    """

    # 1. 根据 n 生成测试数据
    # 这里示例生成：
    # A[i] 在 [1, 10^6] 之间的正整数
    # B[i] 在 [1, 10^3] 之间的正整数
    # 如需可复现结果，可固定种子，例如 random.seed(0)
    random.seed(0)
    A = [random.randint(1, 10**6) for _ in range(n)]
    B = [random.randint(1, 10**3) for _ in range(n)]

    # 2. 原始逻辑（去除 input()），直接使用生成的 A, B
    hp = [(0, 0)]
    dis = {0: 0}
    seen = set()

    while hp:
        _, x = heappop(hp)
        if x == 1:
            print(dis[x])
            break
        if x in seen:
            continue
        seen.add(x)
        for a, b in zip(A, B):
            y = gcd(x, a)
            if y not in dis or dis[y] > dis[x] + b:
                dis[y] = dis[x] + b
                heappush(hp, (dis[y], y))
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：运行规模为 n=5 的测试
    main(5)
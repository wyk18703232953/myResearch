from math import ceil, log
from heapq import heappop, heappush, heapify
import random

def main(n):
    # 生成测试数据
    # 规模 n：数组长度
    # k 为 1 到 n 之间的随机整数
    k = random.randint(1, n)
    # p 和 c 为 1..10^9 范围内的随机正整数
    p = [random.randint(1, 10**9) for _ in range(n)]
    c = [random.randint(1, 10**9) for _ in range(n)]

    # 原有逻辑开始
    arr = [i for i in sorted(enumerate(p), key=lambda x: x[1])]
    maxcoins = [0 for _ in range(k)]
    heapify(maxcoins)
    ans = list(p)
    tmpSum = 0
    tmpSum2 = 0
    prev = arr[0][1]
    for ind, power in arr:
        if power > prev:
            ans[ind] = tmpSum + c[ind]
            tmpSum2 = tmpSum
            prev = power
        else:
            ans[ind] = tmpSum2 + c[ind]
        heappush(maxcoins, c[ind])
        tmpSum += c[ind]
        tmpSum -= heappop(maxcoins)

    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模
    main(10)
import heapq
import random

def main(n, k=None, seed=0):
    random.seed(seed)

    # 若未给出 k，则从 [1, n] 中随机选择
    if k is None:
        k = random.randint(1, n)

    # 生成测试数据：
    # P: 1..10^9 之间的随机整数
    # C: 1..10^9 之间的随机整数
    P = [random.randint(1, 10**9) for _ in range(n)]
    C = [random.randint(1, 10**9) for _ in range(n)]

    X = []
    for i in range(n):
        X.append([P[i], C[i], i])
    X.sort(key=lambda x: x[0])

    coins = []
    heapq.heapify(coins)
    curr = 0
    res = [0 for _ in range(n)]

    limit = min(k, n)
    for i in range(limit):
        heapq.heappush(coins, X[i][1])
        curr += X[i][1]
        res[X[i][2]] = curr

    for j in range(limit, n):
        res[X[j][2]] = X[j][1] + sum(coins)
        if coins:
            x = heapq.heappop(coins)
            if x < X[j][1]:
                heapq.heappush(coins, X[j][1])
            else:
                heapq.heappush(coins, x)

    print(*res)


if __name__ == "__main__":
    # 示例调用：规模 n=10，k 未显式给出则随机生成
    main(10)
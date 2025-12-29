import heapq
import random

def main(n):
    # 生成测试数据
    # n: 元素个数
    # k: 从 [0, n] 中随机选取
    # p: 1..10^9 的随机排列（或一般随机数组）
    # c: 1..10^3 的随机权重
    k = random.randint(0, n) if n > 0 else 0
    p = [random.randint(1, 10**9) for _ in range(n)]
    c = [random.randint(1, 10**3) for _ in range(n)]

    sortedp = sorted([(pi, i) for (i, pi) in enumerate(p)])

    ans = [0 for _ in range(n)]
    acc_coins = 0
    acc = []

    if k == 0:
        print(' '.join(map(str, c)))
    else:
        for i in range(n):
            idx = sortedp[i][1]
            coins = c[idx]
            ans[idx] += acc_coins + coins
            if len(acc) < k:
                acc_coins += coins
                heapq.heappush(acc, coins)
            else:
                smallest_coin = acc[0]  # 堆顶即最小值
                if smallest_coin < coins:
                    acc_coins -= smallest_coin
                    heapq.heapreplace(acc, coins)
                    acc_coins += coins
        print(' '.join(map(str, ans)))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
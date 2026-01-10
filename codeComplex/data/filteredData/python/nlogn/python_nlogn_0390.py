import heapq

def main(n):
    # 解释输入结构：
    # 原程序输入：
    # n, k
    # p[0..n-1]
    # c[0..n-1]
    #
    # 这里将 n 作为数组长度规模
    # 同时构造一个与 n 相关的 k，使得行为有代表性
    # 例如令 k = n // 3（可覆盖 k=0、k<n、k>=n 等情况）
    if n <= 0:
        return

    k = n // 3

    # 确定性生成 p 和 c
    # p 是一个排列（保证排序有意义）
    # c 是与下标相关的确定性整数序列
    p = [(i * 7 + 3) % n for i in range(n)]
    c = [i * 2 + (i // 3) for i in range(n)]

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
                smallest_coin = acc[0]
                if smallest_coin < coins:
                    acc_coins -= smallest_coin
                    heapq.heapreplace(acc, coins)
                    acc_coins += coins
        print(' '.join(map(str, ans)))


if __name__ == "__main__":
    main(10)
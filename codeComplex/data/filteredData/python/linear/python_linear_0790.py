import random

def main(n):
    # 生成测试数据：长度为 n 的 01 串，以及参数 k（1 <= k <= n）
    # 这里示例为：随机生成 cards，k 随机取值。实际需要可按需修改生成策略。
    k = random.randint(1, n)
    cards = ''.join(random.choice('01') for _ in range(n))

    # 原逻辑开始
    def sum_range(l, r, prefix_sum):
        if r < l:
            return 0
        if l == 0:
            return prefix_sum[r]
        return prefix_sum[r] - prefix_sum[l - 1]

    prefix_sum = [0] * n
    prefix_sum[0] = 1 if cards[0] == '1' else 0
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + (1 if cards[i] == '1' else 0)

    min0 = min1 = n
    max0 = max1 = -1
    for i in range(n):
        if cards[i] == '1':
            min1 = min(min1, i)
            max1 = i
        else:
            min0 = min(min0, i)
            max0 = i

    toki = False
    qual = True
    for i in range(0, n - k + 1):
        if sum_range(0, i - 1, prefix_sum) + sum_range(i + k, n - 1, prefix_sum) + k == n:
            toki = True
        if sum_range(0, i - 1, prefix_sum) + sum_range(i + k, n - 1, prefix_sum) == 0:
            toki = True

        prefix = sum_range(0, i - 1, prefix_sum) == 0
        suffix = sum_range(i + k, n - 1, prefix_sum) == 0
        if i > 0 and i + k < n and (prefix ^ suffix) == 0:
            qual = False
        if (min0 < n and (i - min0 > k)) or \
           (min1 < n and (i - min1 > k)) or \
           (max0 >= 0 and (max0 - (i + k - 1) > k)) or \
           (max1 >= 0 and (max1 - (i + k - 1) > k)):
            qual = False

    if toki:
        print('tokitsukaze')
    elif qual:
        print('quailty')
    else:
        print('once again')


if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)
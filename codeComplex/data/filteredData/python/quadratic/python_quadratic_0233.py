from collections import Counter
import random

def makedict(var):
    return dict(Counter(var))

def main(n):
    # 生成测试数据：长度为 n 的 indices 和 cost
    # indices 为 1..(2n) 之间的随机数，保证有一定随机性
    # cost 为 1..100 之间的随机正整数
    if n <= 0:
        print(-1)
        return

    indices = [random.randint(1, 2 * n) for _ in range(n)]
    cost = [random.randint(1, 100) for _ in range(n)]

    ans = float('inf')
    mint = []

    for i in range(n):
        ans = float('inf')
        total = cost[i]
        flag = 0
        for j in range(i):
            if indices[i] > indices[j]:
                ans = min(ans, cost[j])
                flag = 1
        if flag != 0:
            total += ans
            ans = float('inf')
            flag = 0
            for k in range(i + 1, n):
                if indices[k] > indices[i]:
                    ans = min(ans, cost[k])
                    flag = 1
            if flag != 0:
                total += ans
                mint.append(total)
            else:
                continue
        else:
            continue

    if len(mint) > 0:
        print(min(mint))
    else:
        print(-1)

# 示例调用
# main(5)
import random

def main(n):
    # 生成测试数据：随机生成 d 和 k，确保在合法范围内
    # 这里简单设定：1 <= d < n，2 <= k <= max(2, min(5, n-1))
    if n < 2:
        return

    d = random.randint(1, max(1, n - 1))
    k = random.randint(2, max(2, min(5, n - 1)))

    # 原始逻辑开始
    if n == 2 and d == 1 and k == 1:
        print("YES")
        print("1 2")
        return

    if n == d + 1 and k - 1:
        print("YES")
        for i in range(1, d + 1):
            print(i, i + 1)
        return

    if n < d + 1 or k <= 2 or d == 1:
        print("NO")
        return

    if d % 2 == 0:
        if n * (k - 2) > -2 + k * (k - 1) ** (d // 2):
            print("NO")
            return
        print("YES")
        for i in range(1, d + 1):
            print(i, i + 1)
        nodes = d + 1
        leaves = [1 + d // 2]
        dev = 0
        while True:
            new_leaves = []
            for i in leaves:
                for _ in range(k - 1 - (i <= d + 1)):
                    nodes += 1
                    print(i, nodes)
                    new_leaves.append(nodes)
                    if nodes == n:
                        return
            dev += 1
            leaves = new_leaves + [1 - dev + d // 2, 1 + dev + d // 2]
    else:
        if n * (k - 2) > -2 + k * (k - 1) ** (d // 2) + (k - 2) * (k - 1) ** (d // 2):
            print("NO")
            return
        print("YES")
        for i in range(1, d + 1):
            print(i, i + 1)
        nodes = d + 1
        leaves = [1 + d // 2, 2 + d // 2]
        dev = 0
        while True:
            new_leaves = []
            for i in leaves:
                for _ in range(k - 1 - (i <= d + 1)):
                    nodes += 1
                    print(i, nodes)
                    new_leaves.append(nodes)
                    if nodes == n:
                        return
            dev += 1
            leaves = new_leaves + [1 - dev + d // 2, 2 + dev + d // 2]


# 示例调用（实际评测时由外部调用 main(n)）
# main(10)
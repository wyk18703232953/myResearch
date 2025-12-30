import random

class Knight:
    def __init__(self, andis, p, c):
        self.p = int(p)
        self.c = int(c)
        self.andis = int(andis)
        self.ans = self.c

def main(n):
    # 生成测试数据：
    # m 在 [0, n] 之间
    m = random.randint(0, n)

    # 生成 p 和 c，取值范围自行设定，例如 [1, 10^9]
    p = [random.randint(1, 10**9) for _ in range(n)]
    c = [random.randint(1, 10**9) for _ in range(n)]

    # 原始逻辑开始
    x = []
    for i in range(n):
        x.append(Knight(i, p[i], c[i]))

    x.sort(key=lambda x: x.p)
    coins = []
    for i in range(n - 1):
        if len(coins) < m:
            coins.append(x[i].c)
            coins.sort()
        elif len(coins) > 0:
            if coins[0] < x[i].c:
                coins[0] = x[i].c
                coins.sort()
        x[i + 1].ans += sum(coins)

    x.sort(key=lambda x: x.andis)
    for k in x:
        print(k.ans, end=' ')

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)
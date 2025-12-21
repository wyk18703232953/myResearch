import random

def main(n):
    k = random.randint(0, n) if n > 0 else 0
    knight = [random.randint(1, 10**9) for _ in range(n)]
    coins = [random.randint(1, 10**6) for _ in range(n)]
    d = {}
    ans = [0] * n
    for i in range(n):
        knight[i] = [knight[i], i]
    for i in coins:
        d[i] = d.get(i, 0) + 1
    c = coins[:]
    knight = sorted(knight, key=lambda x: x[0])
    ans2 = []
    ans = coins[:]
    if k == 0:
        return ans
    else:
        for i in range(n):
            ans1 = 0
            if len(ans2) < k:
                ans1 = sum(ans2)
            else:
                ans2 = sorted(ans2)[-k:]
                ans1 += sum(ans2)
            ans[knight[i][1]] += ans1
            ans2.append(coins[knight[i][1]])
        return ans

if __name__ == "__main__":
    res = main(10)
    print(*res)
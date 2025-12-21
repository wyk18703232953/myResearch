def count_bits(x):
    ans = 0
    while x:
        x &= x - 1
        ans += 1
    return ans

def main(n):
    import random
    random.seed(0)
    a = [[random.random() for _ in range(n)] for _ in range(n)]
    y = 1 << n
    dp = [0.0] * (y - 1) + [1.0]
    powe = [1 << i for i in range(n)]
    for i in range(y - 1, 0, -1):
        bit = count_bits(i)
        if bit < 2:
            continue
        prob = bit * (bit - 1) // 2
        for j in range(n):
            if not i & powe[j]:
                continue
            for x in range(n):
                if not i & powe[x]:
                    continue
                dp[i - powe[x]] += dp[i] * a[j][x] * prob
                dp[i - powe[j]] += dp[i] * a[x][j] * prob
    z = sum(dp[1 << i] for i in range(n))
    res = [dp[1 << i] / z for i in range(n)]
    for v in res:
        print(v, end=" ")
    print()
    return res

if __name__ == "__main__":
    main(3)
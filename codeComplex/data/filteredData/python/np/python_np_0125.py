import math

def main(n):
    # n 表示数组规模
    b = [i + 2 for i in range(n)]
    c = [i % 5 + 1 for i in range(n)]

    dp = {0: 0}
    s = {0}

    for i in range(n):
        new_dp = dict(dp)
        for j in s:
            g = math.gcd(j, b[i])
            cost = dp[j] + c[i]
            if g in new_dp:
                if cost < new_dp[g]:
                    new_dp[g] = cost
            else:
                new_dp[g] = cost
        dp = new_dp
        s = set(dp.keys())

    if 1 in dp:
        print(dp[1])
    else:
        print(-1)


if __name__ == "__main__":
    main(10)
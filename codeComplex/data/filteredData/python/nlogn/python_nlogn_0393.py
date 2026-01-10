def main(n):
    # Interpret n as the number of people
    # Deterministically generate k, power, coins
    if n <= 0:
        return

    # Choose k as a deterministic function of n, e.g., k = max(1, n // 3)
    k = max(1, n // 3)

    # Deterministic generation of power and coins
    # power: strictly increasing to avoid ties, e.g., i * 2 + 1
    power = [2 * i + 1 for i in range(n)]
    # coins: some deterministic varying pattern
    coins = [(i * 3 + 7) % (2 * n + 5) + 1 for i in range(n)]

    dp = [0 for _ in range(n)]

    def takeSecond(elem):
        return elem[1]

    def takeFirst(elem):
        return elem[0]

    people = [(power[i], coins[i], i) for i in range(n)]

    people.sort(key=takeFirst)

    dp[0] = []

    for i, _p in enumerate(people):
        if i == 0:
            continue
        kills = [val for val in dp[i - 1]]
        kills.append(people[i - 1][1])

        if len(kills) > k:
            # Remove exactly one minimum value
            min_val = kills[0]
            min_idx = 0
            for idx in range(1, len(kills)):
                if kills[idx] < min_val:
                    min_val = kills[idx]
                    min_idx = idx
            del kills[min_idx]

        dp[i] = kills

    x = [(people[i][2], str(sum(dp[i]) + people[i][1])) for i in range(n)]

    x.sort(key=takeFirst)

    print(" ".join([z[1] for z in x]))


if __name__ == "__main__":
    # Example deterministic call
    main(10)
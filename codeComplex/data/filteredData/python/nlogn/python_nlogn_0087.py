def main(n):
    # Interpret n as number of teams; k is derived deterministically
    if n <= 0:
        print(0)
        return

    # Deterministically choose k based on n, ensuring 1 <= k <= n
    k = max(1, n // 3)

    # Generate deterministic team data: each team has two integers [a, b]
    # Example pattern: a = i % 50 + 1, b = (i * 3) % 100
    teams = [[i % 50 + 1, (i * 3) % 100] for i in range(n)]

    teams.sort(key=lambda x: x[0] * 100 - x[1], reverse=True)

    count = 0
    kth = teams[k - 1][0] * 100 + teams[k - 1][1]
    for t in teams:
        if t[0] * 100 + t[1] == kth:
            count += 1
    print(count)


if __name__ == "__main__":
    main(10)
def main(n):
    # Ensure n is at least 1 to avoid empty structures
    if n <= 0:
        return

    # Deterministic generation of le and ri based on n
    # Pattern: le[i] = i % (n // 2 + 1), ri[i] = (n - 1 - i) % (n // 2 + 1)
    base = n // 2 + 1
    le = [(i % base) for i in range(n)]
    ri = [((n - 1 - i) % base) for i in range(n)]

    notp = False
    check = []
    for i in range(n):
        check.append(n - le[i] - ri[i])

    for i in range(n):
        tot = 0
        for j in range(i - 1, -1, -1):
            if check[j] > check[i]:
                tot += 1
        if tot != le[i]:
            notp = True
            break

    if not notp:
        for i in range(n):
            tot = 0
            for j in range(i + 1, n):
                if check[j] > check[i]:
                    tot += 1
            if tot != ri[i]:
                notp = True
                break

    if notp:
        print('NO')
    else:
        print('YES')
        print(*check)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)
def main(n):
    # Interpret n as the number of (manan, surbhi) pairs.
    # Define k deterministically as roughly half of n, at least 1 and at most n.
    if n <= 0:
        return
    k = max(1, min(n, n // 2))

    # Deterministic data generation for l: list of (manan, surbhi) pairs
    # Example pattern:
    # manan varies slowly, surbhi varies more frequently to create ties.
    l = []
    for i in range(n):
        manan = i // 3
        surbhi = (i * 2) % (n // 2 + 1 if n // 2 + 1 > 0 else 1)
        l.append((manan, surbhi))

    # Core logic from original code
    l.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    ans = 1
    ps = l[k - 1][0]
    tp = l[k - 1][1]
    for i in range(k, n):
        if l[i][0] == ps and l[i][1] == tp:
            ans += 1

        else:
            break
    for i in range(k - 2, -1, -1):
        if l[i][0] == ps and l[i][1] == tp:
            ans += 1

        else:
            break

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
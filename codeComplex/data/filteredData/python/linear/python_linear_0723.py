def main(n):
    # Interpret n as the size parameter:
    # n = number of elements in B and G (with original relation m = len(G))
    # Ensure n is at least 1 to avoid empty input
    if n <= 0:
        return

    # Deterministic construction of B and G based on n
    # B is a non-decreasing sequence
    B = [(i // 2) + 1 for i in range(n)]
    # G is constructed to always satisfy min(G) >= max(B)
    z = max(B)
    G = [z + (i % 3) for i in range(n)]

    m = len(G)

    if min(G) < max(B):
        print(-1)
        return

    cnt = 0
    z = max(B)
    y = 0
    f = 1
    f2 = 0
    for i in B:
        if i != z or f2:
            y = max(y, i)
        else:
            f2 = 1
    for i in G:
        if i == z:
            f = 0
        cnt += i - z
    if f:
        cnt += z - y
    print(cnt + sum(B) * m)


if __name__ == "__main__":
    main(10)
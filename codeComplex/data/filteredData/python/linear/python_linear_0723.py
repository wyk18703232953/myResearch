def main(n):
    # Deterministic scalable data generation
    # Interpret n as both length of B and G; also use it as m
    # Ensure n >= 1
    if n <= 0:
        return

    m = n
    # Generate B: increasing small integers
    B = [i % 7 + 1 for i in range(n)]
    # Generate G: ensure min(G) >= max(B) to avoid trivial -1 in most cases
    z = max(B)
    G = [z + (i % 5) for i in range(n)]

    if min(G) < max(B):
        # print(-1)
        pass
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
    # print(cnt + sum(B) * m)
    pass
if __name__ == "__main__":
    main(1000)
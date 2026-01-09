def main(n):
    # Ensure n is at least 1 to avoid empty structures
    if n <= 0:
        return

    # Deterministic data generation
    # l: strictly increasing sequence ensures l[i] > l[j] when i > j
    l = [i for i in range(1, n + 1)]
    # l2: simple deterministic pattern
    l2 = [(i * 2 + 1) for i in range(n)]

    dp_1 = l2.copy()
    INF = 9999999999
    dp_2 = [INF] * n
    dp_3 = [INF] * n

    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j]:
                dp_2[i] = min(dp_2[i], dp_1[j] + l2[i])

    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j]:
                dp_3[i] = min(dp_3[i], dp_2[j] + l2[i])

    x = min(dp_3)
    if x == INF:
        # print(-1)
        pass

    else:
        # print(x)
        pass
if __name__ == "__main__":
    main(10)
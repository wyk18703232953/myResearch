def main(n):
    # Interpret n as: array length = n, k = max(1, n//3)
    k = max(1, n // 3)
    # Deterministic data generation: values[i] cycles through 1..(k+1)
    values = [(i % (k + 1)) + 1 for i in range(n)]

    single, l, r = set(), -1, -1
    for i in range(n):
        single.add(values[i])
        if len(single) == k:
            l, r = 1, i + 1
            break

    single = set()
    for i in range(r - 1, max(-1, l - 2), -1):
        single.add(values[i])
        if len(single) == k:
            l = i + 1
            break

    if len(single) < k:
        # print(-1, -1)
        pass

    else:
        # print(l, r)
        pass
if __name__ == "__main__":
    main(10)
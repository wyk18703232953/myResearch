def main(n):
    # Interpret n as both array length and k (number of distinct values to look for)
    if n <= 0:
        print(-1, -1)
        return

    # Deterministically generate array of length n with values from 1 to n
    values = [(i % n) + 1 for i in range(n)]
    k = n

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
        print(-1, -1)
    else:
        print(l, r)


if __name__ == "__main__":
    # Example deterministic call
    main(10)
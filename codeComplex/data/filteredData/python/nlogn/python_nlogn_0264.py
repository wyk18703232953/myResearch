def main(n):
    # Deterministic data generation:
    # Generate n pairs (l, r) such that:
    # l = i
    # r = n - i + 1
    # This provides varying overlapping intervals for complexity testing.
    a = []
    for i in range(1, n + 1):
        l = i
        r = n - i + 1
        a.append([l, -r, i])

    if n == 0:
        # print(-1, -1)
        pass
        return

    a.sort()
    ma = a[0][1]
    nma = a[0][2]
    for i in range(1, n):
        if a[i][1] >= ma:
            # print(a[i][2], nma)
            pass
            return

        else:
            ma = a[i][1]
            nma = a[i][2]
    # print(-1, -1)
    pass
if __name__ == "__main__":
    main(10)
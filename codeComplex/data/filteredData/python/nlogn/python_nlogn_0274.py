def main(n):
    # Deterministically generate n intervals (l, r)
    # Example pattern: l = i, r = i + (i % 5) to create overlaps and equal starts
    a = []
    for i in range(1, n + 1):
        l = i
        r = i + (i % 5)
        a.append((l, r, i))

    a.sort()

    for i in range(n - 1):
        if a[i][0] == a[i + 1][0]:
            print(str(a[i][2]) + ' ' + str(a[i + 1][2]))
            break

        if a[i][1] >= a[i + 1][1]:
            print(str(a[i + 1][2]) + ' ' + str(a[i][2]))
            break
    else:
        print('-1 -1')


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)
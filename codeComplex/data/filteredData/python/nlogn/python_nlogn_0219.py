def main(n):
    if n < 3:
        print(-1)
        return
    U = n // 2
    E = [i * 2 for i in range(n)]
    mmax = -1
    for i in range(0, n - 2):
        j = i + 1
        l = j + 1
        r = n - 1
        while l < r:
            mid = (l + r) // 2
            if E[mid] - E[i] <= U:
                l = mid + 1
            else:
                r = mid - 1
        if E[l] - E[i] <= U:
            if E[l] - E[i] != 0:
                cur = (E[l] - E[j]) / (E[l] - E[i])
                mmax = max(mmax, cur)
        else:
            if l - 1 > j and E[l - 1] - E[i] <= U and E[l - 1] - E[i] != 0:
                cur = (E[l - 1] - E[j]) / (E[l - 1] - E[i])
                mmax = max(mmax, cur)
    print(mmax)


if __name__ == "__main__":
    main(1000)
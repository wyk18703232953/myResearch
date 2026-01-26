def main(n):
    # Generate deterministic input array 'a' of length 2*n with values in [1, n]
    # Pattern: a[2*i] = (i % n) + 1, a[2*i+1] = ((i + n//2) % n) + 1
    # This ensures each value appears at least once; for n>1 many appear twice.
    l = [-1] * n
    r = [-1] * n
    a = [((i // 2 + (i % 2) * (n // 2)) % n) + 1 for i in range(2 * n)]

    for i in range(2 * n):
        x = a[i] - 1
        if l[x] == -1:
            l[x] = i
        r[x] = i

    ans = 0
    for i in range(n):
        for j in range(n):
            if l[i] < l[j] < r[j] < r[i]:
                ans += 2
    for i in range(n):
        ans += r[i] - l[i] - 1
    result = ans // 2
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(5)
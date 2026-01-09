def main(n):
    # Deterministically generate n, k, and array a based on n
    # Keep values within 0..255 because c has size 256
    k = max(1, (n // 3) % 256)
    a = [(i * 7 + 3) % 256 for i in range(n)]

    c = [-1] * 256
    ans = [0] * n

    for i in range(n):
        if c[a[i]] == -1:
            for j in range(a[i], max(-1, a[i] - k), -1):
                if c[j] != -1:
                    if (c[j] + k) > a[i]:
                        c[a[i]] = c[j]

                    else:
                        c[a[i]] = j + 1
                    break
            if c[a[i]] == -1:
                c[a[i]] = max(0, a[i] - k + 1)
            for xx in range(c[a[i]], a[i]):
                c[xx] = c[a[i]]
        ans[i] = str(c[a[i]])

    # print(' '.join(ans))
    pass
if __name__ == "__main__":
    main(10)
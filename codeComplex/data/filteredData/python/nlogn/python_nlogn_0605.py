def main(n):
    # Interpret n as the size of the array (originally n)
    # We also need an m (unused in the logic), define it deterministically
    m = n + 5

    # Deterministic generation of the list 'a' of length n
    # Example pattern: a[i] = (i * 3) % (n + 7) + 1
    a = [0] + [((i * 3) % (n + 7)) + 1 for i in range(1, n + 1)]

    # Core logic preserved
    a.sort()
    ans = 0
    h = a[-1]
    for i in range(n, 0, -1):
        if a[i - 1] < h - 1:
            ans = ans + a[i] - h + a[i - 1]
            h = a[i - 1]

        else:
            ans = ans + a[i] - 1
            h = h - 1
    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call
    main(10)
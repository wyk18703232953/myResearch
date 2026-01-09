def main(n):
    if n < 2:
        # print(0)
        pass
        return
    a = [(i * 3 + 1) % (5 * n + 7) + 1 for i in range(n)]
    k = min(a[0], a[-1]) // (n - 1)
    for i in range(1, n - 1):
        k = min(k, min(a[0], a[i]) // i, min(a[i], a[-1]) // (n - 1 - i))
    # print(k)
    pass
if __name__ == "__main__":
    main(10)
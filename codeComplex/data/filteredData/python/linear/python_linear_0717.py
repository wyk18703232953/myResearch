def main(n):
    # generate deterministic array a of length n
    a = [(i * 3 + 5) for i in range(n)]
    max1 = float('inf')
    for q in range(len(a)):
        if q != 0 and q >= n - q - 1:
            max1 = min(max1, min(a[q], a[0]) // q)
        if n - q - 1 != 0 and q <= n - q - 1:
            max1 = min(max1, min(a[q], a[-1]) // (n - q - 1))
    # print(max1)
    pass
if __name__ == "__main__":
    main(10)
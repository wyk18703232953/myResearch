def main(n):
    # Deterministic parameter generation based on n
    l = n
    r = n * (n + 1) // 2  # sum of 1..n
    x = max(1, n // 3)
    C = [i + 1 for i in range(n)]

    k = 0
    for i in range(1, 2 ** n):  # skip empty subset since max/min undefined
        W = [w for w, b in zip(C, bin(i)[2:].zfill(n)) if b == '1']
        s = sum(W)
        if l <= s <= r and max(W) - min(W) >= x:
            k += 1
    print(k)


if __name__ == "__main__":
    main(10)
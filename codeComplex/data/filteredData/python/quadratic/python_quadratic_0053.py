def main(n):
    # Interpret n as array length; set m = n for scalability
    a = [(i * 2 + 1) % (2 * n + 1) for i in range(n)]
    m = n

    parity = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                parity ^= 1

    res = []
    for i in range(m):
        l = i % n
        r = n - 1 - (i % n)
        if l > r:
            l, r = r, l
        s = r - l + 1
        parity ^= (s * (s - 1) // 2) % 2
        res.append("odd" if parity else "even")

    # print("\n".join(res))
    pass
if __name__ == "__main__":
    main(1000)
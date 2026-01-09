def main(n):
    # Interpret n as both the size of k and p
    # Generate deterministic test data
    # k is a non-decreasing sequence
    k = [i // 2 for i in range(n)]
    # p is another sequence designed to have mixed >= relations
    p = [(i * 3) // 4 for i in range(n)]

    m = len(p)

    a = 0
    b = 0
    ans = 0
    while a != n and b != m:
        if p[b] >= k[a]:
            ans += 1
            a += 1
            b += 1

        else:
            a += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
def main(n):
    # Generate deterministic test data:
    # a and b are permutations of 1..n with a simple pattern
    a = [((i * 2) % n) + 1 for i in range(n)]
    # Ensure it's a permutation by fixing possible duplicates when n is even
    # but since ((i*2)%n) for i in 0..n-1 is a permutation when n and 2 are coprime,
    # for even n, adjust with a simple deterministic shuffle-like transform
    if n % 2 == 0:
        a = list(range(1, n + 1))
        a = a[::-1]
    b = [((i * 3) % n) + 1 for i in range(n)]
    if n % 3 == 0:
        b = list(range(1, n + 1))

    a = a[::-1]
    c = [0] * n
    bk = []
    for i in range(n):
        co = 0
        if c[b[i] - 1] == 0:
            while a and a[-1] != b[i]:
                co += 1
                c[a[-1] - 1] = 1
                a.pop()
            if a:
                co += 1
                c[a[-1] - 1] = 1
                a.pop()
        bk.append(co)
    # print(*bk)
    pass
if __name__ == "__main__":
    main(10)
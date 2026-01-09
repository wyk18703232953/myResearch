M = 998244353

def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    l = list(range(n, 0, -1))
    l.sort()
    l = l[::-1]
    out = [0] * n
    big = 0
    if n >= 2 and l[0] >= 2 * l[1]:
        out[1] = 1
        big = 1
    for i in range(2, n):
        new = [0] * n
        bigN = 0
        for j in range(i):
            if l[j] >= 2 * l[i]:
                big += out[j]

            else:
                new[j] += out[j] * (i - 1)
                new[j] %= M
        new[i] = big
        bigN = (i * big) % M
        out = new
        big = bigN
    # print((big + sum(out)) % M)
    pass
if __name__ == "__main__":
    main(10)
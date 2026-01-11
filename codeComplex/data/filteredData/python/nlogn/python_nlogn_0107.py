def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def prefix_sum(arr):
    r = [0] * (len(arr) + 1)
    for i, el in enumerate(arr):
        r[i + 1] = r[i] + el
    return r


def divideCeil(n, x):
    if n % x == 0:
        return n // x
    return n // x + 1


def main(n):
    t = 1
    for _ in range(t):
        size = n
        l = [(i * 2 + 3) % (n + 7) for i in range(size)]
        # introduce a deterministic swap pattern to occasionally create "YES" cases
        if size >= 2 and size % 3 == 0:
            l[0], l[-1] = l[-1], l[0]

        l1 = l[:]
        l1.sort()
        pos = []
        for i in range(size):
            if l1[i] != l[i]:
                pos.append(i)
        if (len(pos) == 0) or (len(pos) == 2 and l[pos[0]] == l1[pos[1]] and l[pos[1]] == l1[pos[0]]):
            # print("YES")
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    main(10)
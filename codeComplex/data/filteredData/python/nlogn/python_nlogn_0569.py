def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)


def bfs(g, d, n):
    for i in range(n, 0, -1):
        while g[i]:
            x = g[i].pop()
            d[i] += d[x]
    return d


def main(n):
    # Generate deterministic input of size n
    # Original input: integer n and list l of length n
    # Here we construct l so that 1 <= l[i] < i to form a tree-like parent array.
    if n <= 0:
        return

    if n == 1:
        print(1)
        return
    if n == 2:
        print(1, 1)
        return

    # l[1..n], construct deterministically:
    # l[1] is unused in original code (list is shifted), so we only need length n
    # For original constraints: for i in 2..n, l[i] is a parent in [1..i-1]
    l = [0] * n
    for i in range(1, n):
        # parent of node i+1 is i//2 + 1 in [1..i]
        l[i] = (i // 2) + 1

    d = [0] * (n + 1)
    # shift as in original: l = [0,0] + l
    l = [0, 0] + l
    from collections import defaultdict
    g = defaultdict(list)
    for i in range(2, n + 1):
        g[l[i]].append(i)
        d[i] += 1
        d[l[i]] += 1
    for i in range(1, n + 1):
        if g[i]:
            d[i] = 0
    x = bfs(g, d, n)
    x.sort()
    for i in range(1, n + 1):
        print(x[i], end=' ')
    print()


if __name__ == "__main__":
    main(10)
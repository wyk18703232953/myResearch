import math

def solve(n, m, a):
    l = -1
    r = 10**9 + 1
    ans1, ans2 = -1, -1
    while r - l > 1:
        x = (l + r) // 2
        idx = {}
        for i in range(n):
            v = 0
            for j in range(m):
                if a[i][j] >= x:
                    v += 1
                v <<= 1
            idx[v >> 1] = i
        ok = False
        idx1, idx2 = 0, 0
        full = (1 << m) - 1
        for aa, bb in idx.items():
            for cc, dd in idx.items():
                for _ in range(m):
                    if (aa | cc) == full:
                        ok = True
                        idx1 = bb + 1
                        idx2 = dd + 1
        if ok:
            l = x
            ans1 = idx1
            ans2 = idx2
        else:
            r = x
    return ans1, ans2

def generate_input(n):
    if n <= 0:
        n = 1
    m = max(1, n // 2)
    a = [[(i * m + j) % (10**9 + 7) for j in range(m)] for i in range(n)]
    return n, m, a

def main(n):
    n, m, a = generate_input(n)
    ans1, ans2 = solve(n, m, a)
    print(ans1, ans2)

if __name__ == "__main__":
    main(5)
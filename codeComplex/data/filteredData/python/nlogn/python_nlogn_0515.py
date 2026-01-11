from collections import defaultdict

def solve_one(a):
    n = len(a)
    dd = defaultdict(int)
    for i in range(n):
        dd[a[i]] += 1
    l = []
    for aa in a:
        if dd[aa] >= 2:
            l.append(aa)
            dd[aa] -= 2
    l.sort()
    ans = [-1, -1, -1, -1]
    m = 10**18
    for i in range(len(l) - 1):
        x = (4 * (l[i] + l[i + 1]) ** 2) / (l[i] * l[i + 1])
        if x < m:
            ans = [l[i], l[i], l[i + 1], l[i + 1]]
            m = x
    return ans

def main(n):
    t = n
    results = []
    for k in range(1, t + 1):
        size = max(4, k)
        a = [(i % (k + 3)) + 1 for i in range(size)]
        res = solve_one(a)
        results.append(res)
    for r in results:
        # print(*r)
        pass
if __name__ == "__main__":
    main(5)
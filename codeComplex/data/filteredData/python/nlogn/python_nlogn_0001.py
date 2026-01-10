def good(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    return x2 >= y1

def solve(n, t, x, a):
    def check(cent):
        for i in range(n):
            if not good(cent - t, cent + t, x[i] - a[i], x[i] + a[i]):
                return 0
        return 1

    ans = set()
    for i in range(n):
        val1 = x[i] - a[i] - t
        val2 = x[i] + a[i] + t
        if check(val1):
            ans.add(val1)
        if check(val2):
            ans.add(val2)
    return len(ans)

def main(n):
    t = n // 2 + 1
    x = [2 * (i + 1) for i in range(n)]
    a = [(i % 5) + 1 for i in range(n)]
    result = solve(n, t, x, a)
    print(result)

if __name__ == "__main__":
    main(10)
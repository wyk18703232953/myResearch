import bisect as bi

def find_gt(a, x):
    i = bi.bisect_left(a, x)
    if i != len(a):
        return i
    else:
        return len(a)

def solve(intervals):
    n = len(intervals)
    points, l = [], []
    for a, b in intervals:
        l.append((a, b))
        points.append(a)
        points.append(b)
    points.sort()
    k = 0
    d = {}
    l1 = []
    for i in range(2 * n):
        if d.get(points[i], -1) == -1:
            d[points[i]] = k
            l1.append(points[i])
            k += 1
    n1 = len(d)
    dp = [[0, 0] for _ in range(n1)]
    for a, b in l:
        dp[d[a]][0] += 1
        dp[d[b]][1] -= 1

    ans = {}
    last = dp[0][0]
    ans[last] = 1
    last += dp[0][1]
    for i in range(1, n1):
        cnts = l1[i] - l1[i - 1] - 1
        if ans.get(last, -1) != -1:
            ans[last] += cnts
        else:
            ans[last] = cnts
        last += dp[i][0]
        if ans.get(last, -1) != -1:
            ans[last] += 1
        else:
            ans[last] = 1
        last += dp[i][1]
    if ans.get(last, -1) != -1:
        ans[last] += 1
    else:
        ans[last] = 1
    res = []
    for i in range(1, n + 1):
        res.append(ans.get(i, 0))
    return res

def main(n):
    # n is the number of intervals
    # Deterministic generation of intervals: [ (i, 2*i+1) for i in range(1, n+1) ]
    intervals = [(i, 2 * i + 1) for i in range(1, n + 1)]
    res = solve(intervals)
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    main(10)
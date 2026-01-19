from collections import defaultdict

def check(mid, m, a):
    d = defaultdict(int)
    for idx, row in enumerate(a):
        string = ''
        for val in row:
            if val >= mid:
                string += '1'
            else:
                string += '0'
        d[int(string, 2)] = idx
    full = (1 << m) - 1
    for i in d.keys():
        for j in d.keys():
            if i | j == full:
                return [d[i], d[j]]
    return []

def binarySearch(lo, hi, m, a):
    ans = []
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        x = check(mid, m, a)
        if x:
            lo = mid
            ans = [x[0] + 1, x[1] + 1]
        else:
            hi = mid - 1
    mid = lo + (hi - lo + 1) // 2
    x = check(mid, m, a)
    if x:
        ans = [x[0] + 1, x[1] + 1]
    return ans

def generate_data(n):
    # Map n to matrix size: choose m = max(1, min(20, n))
    # Number of rows equals n, number of columns equals m
    m = max(1, min(20, n))
    a = []
    for i in range(n):
        row = []
        for j in range(m):
            val = (i + 1) * (j + 2)
            row.append(val)
        a.append(row)
    return n, m, a

def main(n):
    n, m, a = generate_data(n)
    res = binarySearch(0, 10**9, m, a)
    print(*res)

if __name__ == "__main__":
    main(10)
from collections import defaultdict

def check(mid, m, a, n):
    d = defaultdict(int)
    for idx in range(n):
        row = a[idx]
        string = []
        for val in row:
            if val >= mid:
                string.append('1')
            else:
                string.append('0')
        key = int(''.join(string), 2)
        d[key] = idx
    full = (1 << m) - 1
    keys = list(d.keys())
    for i in keys:
        for j in keys:
            if (i | j) == full:
                return [d[i], d[j]]
    return []

def binarySearch(lo, hi, m, a, n):
    ans = []
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        x = check(mid, m, a, n)
        if x:
            lo = mid
            ans = [x[0] + 1, x[1] + 1]
        else:
            hi = mid - 1
    mid = lo + (hi - lo + 1) // 2
    x = check(mid, m, a, n)
    if x:
        ans = [x[0] + 1, x[1] + 1]
    return ans

def generate_data(n):
    # Interpret n as the number of rows; set m (number of columns) as max(1, n // 2)
    m = max(1, n // 2)
    a = []
    for i in range(n):
        row = []
        for j in range(m):
            # Deterministic value depending on i and j
            row.append((i * 131 + j * 17) % 1000000000
                       + (i // 2) * 7
                       + (j // 3) * 5)
        a.append(row)
    return n, m, a

def main(n):
    n, m, a = generate_data(n)
    res = binarySearch(0, 10**9, m, a, n)
    if res:
        print(res[0], res[1])
    else:
        print(-1, -1)

if __name__ == "__main__":
    main(10)
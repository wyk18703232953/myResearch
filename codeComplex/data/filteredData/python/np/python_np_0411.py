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
    return ans

def generate_input(n):
    # Interpret n as number of rows; number of columns m grows slowly with n
    # Ensure m >= 1
    m = max(1, (n % 7) + 1)
    a = []
    base = n + 1
    for i in range(n):
        row = []
        for j in range(m):
            # Deterministic arithmetic pattern
            val = (i + 1) * (j + 2) + (i // 2) + (j % 3) + base
            row.append(val)
        a.append(row)
    return n, m, a

def main(n):
    n, m, a = generate_input(n)
    result = binarySearch(-1, 10**9 + 1, m, a)
    if result:
        print(result[0], result[1])
    else:
        print(-1, -1)

if __name__ == "__main__":
    main(10)
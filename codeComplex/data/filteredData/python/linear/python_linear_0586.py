from sys import stdout

mod = 1000000007

def build_queries(n):
    q = n
    queries = []
    for i in range(1, q + 1):
        if i % 2 == 1:
            l = 1
            r = min(n, i)

        else:
            l = max(1, n - i + 1)
            r = n
        if l > r:
            l, r = r, l
        queries.append((l, r))
    return queries

def build_string(n):
    # deterministic binary string of length n
    return ''.join('0' if i % 2 == 0 else '1' for i in range(n))

def main(n):
    if n <= 0:
        return

    q = n
    a = build_string(n)

    o = []
    s = []
    r_zero = 0
    r_one = 0
    for ch in a:
        if ch == '0':
            r_zero += 1

        else:
            r_one += 1
        o.append(r_zero)
        s.append(r_one)

    z = [1]
    for _ in range(100000):
        z.append((z[-1] * 2) % mod)

    queries = build_queries(n)

    out_lines = []
    for (l, r) in queries:
        m = r - l + 1
        zs = o[r - 1] - o[l - 1] + (a[l - 1] == '0')
        os = m - zs
        if zs != 0:
            val = (((z[os] - 1) % mod) * (z[zs] % mod)) % mod

        else:
            val = (z[os] - 1) % mod
        out_lines.append(str(val))

    stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main(10)
def main(n):
    from collections import defaultdict as dc

    # Generate deterministic input list l of size n
    # Example pattern: l[i] = (i % 5) - 2  => values in [-2, -1, 0, 1, 2]
    l = [(i % 5) - 2 for i in range(n)]

    x = dc(int)
    y = dc(int)
    z = dc(int)
    p = dc(int)
    q = dc(int)
    r = dc(int)

    if n == 0:
        print(0)
        return

    x[l[-1]] += 1
    y[l[-1]] += 1
    z[l[-1]] += 1

    for i in range(n - 2, -1, -1):
        p[i] = x[l[i]]
        q[i] = y[l[i] + 1]
        r[i] = z[l[i] - 1]
        x[l[i]] += 1
        y[l[i]] += 1
        z[l[i]] += 1

    x_arr = [0] * n
    for i in range(n - 2, -1, -1):
        x_arr[i] = l[i + 1] + x_arr[i + 1]

    s = 0
    for i in range(n - 2, -1, -1):
        c = x_arr[i] - (p[i] * l[i]) - (q[i] * (l[i] + 1)) - (r[i] * (l[i] - 1))
        d = n - i - 1 - p[i] - q[i] - r[i]
        e = c - l[i] * d
        s += e

    print(s)


if __name__ == "__main__":
    main(10)
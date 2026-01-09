def solve(a, b):
    m = len(a)
    n = len(b)
    p_b = [0]
    for x in b[:]:
        p_b.append(p_b[-1] + int(x))
    s = 0
    for i in range(m):
        if a[i] == '0':
            s += p_b[n - m + 1 + i] - p_b[i]

        else:
            s += (n - m + 1) - (p_b[n - m + 1 + i] - p_b[i])
    return s


def main(n):
    if n < 1:
        n = 1
    m = n
    L = 2 * n
    a = ''.join('0' if i % 2 == 0 else '1' for i in range(m))
    b = ''.join('1' if (i * 3) % 5 < 3 else '0' for i in range(L))
    res = solve(a, b)
    # print(res)
    pass
if __name__ == "__main__":
    main(10)
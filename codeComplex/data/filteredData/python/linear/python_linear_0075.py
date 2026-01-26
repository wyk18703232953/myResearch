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
    if n <= 0:
        return 0
    m = max(1, n // 2)
    if m > n:
        m = n
    a = ''.join(str(i % 2) for i in range(m))
    b = ''.join(str((i // 2) % 2) for i in range(n))
    result = solve(a, b)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)
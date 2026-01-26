def solve(n, m, x, t):
    r = [0] * n
    d = [0] * m
    ans = [0] * m
    cr = 0
    cd = 0
    for i in range(n + m):
        if t[i]:
            d[cd] = x[i]
            cd += 1

        else:
            r[cr] = x[i]
            cr += 1
    cn = 0
    for i in range(m - 1):
        mid = (d[i] + d[i + 1]) // 2
        while cn < n and r[cn] <= mid:
            cn += 1
            ans[i] += 1
    ans[-1] += n - sum(ans)
    return ' '.join(str(i) for i in ans)


def main(n):
    if n < 2:
        n = 2
    # map n to counts of r and d
    num_r = n
    num_d = n
    total = num_r + num_d

    # construct t: first num_d are 'd'(1), rest are 'r'(0)
    t = [1] * num_d + [0] * num_r

    # construct x deterministically: strictly increasing to keep ordering clear
    # d positions first, then r positions, but all in one sequence
    # ensure same length as t
    x = [i for i in range(1, total + 1)]

    res = solve(num_r, num_d, x, t)
    # print(res)
    pass
if __name__ == "__main__":
    main(10)
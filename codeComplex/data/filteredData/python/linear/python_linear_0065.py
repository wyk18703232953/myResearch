def solve(n, p, s):
    p.append((0, 0))
    p.sort()
    t = 0
    while p:
        x = p.pop()
        s, t = x[0], max(x[1], t + abs(s - x[0]))
    return t


def main(n):
    s = n
    p = [(i, i // 2) for i in range(1, n + 1)]
    ans = solve(n, p, s)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
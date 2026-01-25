def main(n):
    # generate deterministic data: a permutation of 0..n-1 duplicated once
    a = [i for i in range(n)] + [i for i in range(n)]
    ans = 0
    pos = 2 * n - 2
    for _ in range(n):
        x = a[-1]
        a.pop(-1)
        y = a.index(x)
        ans += pos - y
        pos -= 2
        a.pop(y)
    print(ans)


if __name__ == "__main__":
    main(5)
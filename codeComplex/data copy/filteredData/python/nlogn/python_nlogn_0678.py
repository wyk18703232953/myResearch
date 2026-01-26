def main(n):
    # n controls the size of b and g (both of length n, with n>=2 for logic to work)
    if n < 2:
        n = 2

    # Deterministic generation of b and g based on n
    # b: increasing small integers
    b = [i % 7 + 1 for i in range(1, n + 1)]
    # g: larger integers to ensure ming is not trivially small
    g = [i % 11 + 5 for i in range(1, n + 1)]

    m = len(g)

    ans = 0
    maxb2, maxb = sorted(b)[-2:]
    ming = min(g)
    if maxb > ming:
        ans = -1

    else:
        ans += sum(b) * m
        ans += (sum(g) - ming) - (maxb * (m - 1))
        if ming > maxb:
            ans += ming - maxb2
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
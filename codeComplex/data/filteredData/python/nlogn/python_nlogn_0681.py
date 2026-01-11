def main(n):
    # Interpret n as both number of boys and girls for scalability
    # Generate deterministic data:
    # b: increasing sequence 1..n
    # g: shift of b with a constant to ensure variety and g[0] >= b[-1] often
    m = n
    if n <= 0:
        return 0

    b = [i + 1 for i in range(n)]
    g = [i + 1 + (n // 2) for i in range(n)]

    b.sort()
    g.sort()
    if b[-1] > g[0]:
        ans = -1

    else:
        ans = sum(b) * m
        if g[0] != b[-1]:
            ans += g[0] - b[-2]
        for i in range(1, m):
            ans += g[i] - b[-1]
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(10)
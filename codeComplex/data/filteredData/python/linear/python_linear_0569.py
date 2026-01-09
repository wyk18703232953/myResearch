def main(n):
    fa = [0, 0] + [i for i in range(1, n - 1)]  # deterministic parent array for n >= 2
    if n <= 1:
        fa = [0, 0][:n + 1]

    delta = [0] * (n + 1)
    suml = [0] * (n + 1)

    for i in range(n, 0, -1):
        if suml[i] == 0:
            suml[i] = 1
        delta[suml[i]] += 1
        if fa[i] >= 0 and fa[i] <= n:
            suml[fa[i]] += suml[i]

    for i in range(1, n + 1):
        delta[i] += delta[i - 1]

    ans = 0
    output = []
    for i in range(1, n + 1):
        while ans <= n and delta[ans] < i:
            ans += 1
        if ans > n:
            ans = n
        output.append(str(ans))
    # print(" ".join(output))
    pass
    # print()
    pass
if __name__ == "__main__":
    main(10)
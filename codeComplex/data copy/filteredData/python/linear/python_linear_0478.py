def main(n):
    if n <= 0:
        return 0

    # Generate deterministic data based on n
    # a will be a permutation with one big cycle (1-based indices)
    a = list(range(2, n + 1)) + [1]
    # c will be some deterministic costs
    c = [(i * 3 + 5) % (n + 7) + 1 for i in range(n)]

    u = [0] * len(a)
    ans = 0

    for i in range(len(a)):
        if u[i] != 0:
            continue
        idx = i
        while u[idx] == 0:
            u[idx] = 1
            idx = a[idx] - 1

        if u[idx] == 2:
            idx = i
            while u[idx] == 1:
                u[idx] = 2
                idx = a[idx] - 1
            continue

        start = idx
        mn = c[idx]
        u[idx] = 2
        while a[idx] - 1 != start:
            idx = a[idx] - 1
            mn = min(mn, c[idx])
            u[idx] = 2

        idx = i
        while u[idx] == 1:
            u[idx] = 2
            idx = a[idx] - 1
        ans += mn

    return ans


if __name__ == "__main__":
    # Example calls for different input scales
    for n in [1, 5, 10, 100]:
        # print(n, main(n))
        pass
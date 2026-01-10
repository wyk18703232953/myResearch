from collections import defaultdict

def main(n):
    # Deterministic data generation
    # n: length of array p
    # m: choose a value that is guaranteed to appear in p
    if n <= 0:
        print(0)
        return

    # Generate p deterministically
    # p[i] = (i % 5) + 1  -> values in [1..5]
    p = [(i % 5) + 1 for i in range(n)]
    # Choose m as a value from p that is sure to appear, e.g., p[n//2]
    m = p[n // 2]

    x = [0] * (n + 1)
    l = 0
    for i in range(n):
        if p[i] < m:
            x[i + 1] = -1
        elif p[i] > m:
            x[i + 1] = 1
        else:
            l = i
    for i in range(1, n + 1):
        x[i] += x[i - 1]
    cnt = [defaultdict(lambda: 0) for _ in range(2)]
    for i in range(l + 1):
        cnt[i % 2][x[i]] += 1
    ans = 0
    for i in range(l + 1, n + 1):
        xi = x[i]
        ans += cnt[i % 2][xi - 1]
        ans += cnt[i % 2 ^ 1][xi]
    print(ans)

if __name__ == "__main__":
    main(10)
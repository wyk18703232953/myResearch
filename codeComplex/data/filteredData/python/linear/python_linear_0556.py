from collections import defaultdict

def main(n):
    k = (n % 20) + 1
    a = [0] + [i % (1 << k) for i in range(1, n + 1)]
    h = defaultdict(int)
    for i in range(n):
        a[i + 1] ^= a[i]
    mask = (1 << k) - 1
    for i in range(n + 1):
        h[min(a[i] ^ mask, a[i])] += 1
    ans = 0
    for _, t in h.items():
        x = t // 2
        y = t - x
        ans += x * (x - 1) // 2 + y * (y - 1) // 2
    ans = (n * (n + 1)) // 2 - ans
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
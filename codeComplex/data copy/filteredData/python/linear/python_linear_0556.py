from collections import defaultdict

def main(n):
    # Deterministic generation of k and array based on n
    if n <= 0:
        # print(0)
        pass
        return

    k = max(1, (n % 20) + 1)  # k in [1, 21], deterministic from n

    # Generate array of length n
    base = (n * 131) % 1000003
    arr = [((base + i * 17) ^ (i * i + 3 * i + 7)) & ((1 << k) - 1) for i in range(n)]

    a = [0] + arr
    h = defaultdict(int)
    for i in range(n):
        a[i + 1] ^= a[i]
    for i in range(n + 1):
        h[min(a[i] ^ ((1 << k) - 1), a[i])] += 1
    ans = 0
    for x, t in h.items():
        pa = t // 2
        pb = t - pa
        ans += pa * (pa - 1) // 2 + pb * (pb - 1) // 2
    ans = (n * (n + 1)) // 2 - ans
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
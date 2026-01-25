from collections import defaultdict

def main(n):
    k = max(1, n // 10)
    arr = [i & ((1 << k) - 1) for i in range(1, n + 1)]
    xors = defaultdict(int)
    xors[0] = 1
    comp = (1 << k) - 1
    ans = n * (n + 1) // 2
    xor = 0
    for a in arr:
        xor ^= a
        if xors[xor] > xors[comp ^ xor]:
            xor ^= comp
        ans -= xors[xor]
        xors[xor] += 1
    print(ans)

if __name__ == "__main__":
    main(1000)
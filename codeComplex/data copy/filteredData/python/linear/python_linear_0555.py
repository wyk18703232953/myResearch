from collections import defaultdict

def main(n):
    # Generate deterministic k and array of length n
    k = 4
    arr = [(i * 3 + 1) % (1 << k) for i in range(n)]

    xors = defaultdict(int)
    xors[0] = 1
    comp = (1 << k) - 1
    xor = 0
    ans = n * (n + 1) // 2
    for a in arr:
        xor ^= a
        if xors[xor] > xors[comp ^ xor]:
            xor ^= comp
        ans -= xors[xor]
        xors[xor] += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
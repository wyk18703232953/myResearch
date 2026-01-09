def main(n):
    # n is the length of the array
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministically generate k and arr based on n
    # Choose k so that values stay reasonable: let k be between 1 and 20
    k = (n % 20) + 1  # 1 <= k <= 20
    comp = (1 << k) - 1

    # Generate an array of length n with values in [0, comp]
    # Use a simple deterministic formula
    arr = [(i * 31 + 7) & comp for i in range(n)]

    from collections import defaultdict

    xors = defaultdict(int)
    xors[0] = 1
    ans = n * (n + 1) // 2
    xor = 0
    for a in arr:
        xor ^= a
        if xors[xor] > xors[comp ^ xor]:
            xor ^= comp
        ans -= xors[xor]
        xors[xor] += 1
    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)
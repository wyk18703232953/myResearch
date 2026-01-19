import math

def main(n):
    # n: length of the list
    if n <= 0:
        return
    N = 22
    size = 1 << N

    # Deterministically generate lis of length n with values in [0, 2^22)
    # Use simple arithmetic patterns to stay within range.
    lis = [(i * 1234567 + 890123) & (size - 1) for i in range(n)]

    dp = [-1] * size

    # Core logic from original program
    # First pass: for each value, store it in dp, then flip all 22 bits
    for i in range(n):
        dp[lis[i]] = lis[i]
        for j in range(N):
            lis[i] ^= (1 << j)

    # SOS-like DP to fill dp for all masks
    for mask in range(size):
        if dp[mask] != -1:
            continue
        m = mask
        # iterate over bits and try to inherit from submasks
        for i in range(N):
            if m & (1 << i):
                prev = m ^ (1 << i)
                if dp[prev] != -1:
                    dp[mask] = dp[prev]
                    break

    # Produce output string (matching original behavior: numbers separated by space, then newline)
    out_parts = []
    for num in lis:
        out_parts.append(str(dp[num]))
    print(" ".join(out_parts))


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)
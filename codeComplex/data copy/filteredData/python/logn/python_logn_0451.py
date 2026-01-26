# Converted version with main(n), no input(), and generated test data.

from itertools import accumulate

def main(n):
    """
    n: problem scale, used here as number of test cases Q.
       For each test case i (0-based), generate:
       N = 10 + i
       K = i * (i + 1) // 2   (any deterministic pattern is fine)
    """
    Q = n

    # Precompute 4^i up to 61 (as original code did)
    four = [1] * 62
    for i in range(1, 62):
        four[i] = four[i - 1] * 4

    for i_case in range(Q):
        # Generate deterministic test data based on scale n and case index
        N = 10 + i_case
        K = i_case * (i_case + 1) // 2

        tmp_N = N
        if N >= 60:
            N = 60

        dk = (4 ** N - 1) // 3
        if K > dk:
            # print('NO')
            pass
            continue

        seq = []
        block = []
        s = 0
        for i in range(N):
            val = 2 ** (i + 1) - 1
            s += val
            block.append(val)
            seq.append(s)

        if K >= seq[-1]:
            # print('YES', 0)
            pass
            continue

        for i in range(N - 1):
            if seq[i] <= K < seq[i + 1]:
                d = K - seq[i]
                happy = tmp_N - i - 1
                round_ = i + 1
                break

        block = block[::-1]
        res = 0
        for i in range(round_):
            A = (4 ** (i + 1) - 1) // 3
            B = block[i] - 2
            res += A * B

        if d <= res:
            # print('YES', happy)
            pass

        else:
            # print('NO')
            pass
if __name__ == "__main__":
    # Example: run main with n = 5 test cases
    main(5)
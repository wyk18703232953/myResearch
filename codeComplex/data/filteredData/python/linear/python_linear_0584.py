import sys

mod = 10**9 + 7

def count(m, n, mod):
    return (pow(2, m, mod) - 1) * pow(2, n, mod) % mod

def main(n):
    # n controls length of S; number of queries q is chosen as n
    N = max(1, n)
    q = N

    # Deterministically generate S as a binary string using i % 2 pattern
    S = ''.join('1' if i % 2 == 0 else '0' for i in range(N))

    # Deterministically generate LR queries
    # For scalability and coverage, create q intervals within [1, N]
    LR = []
    for i in range(1, q + 1):
        l = (i % N) + 1
        r = ((i * 2) % N) + 1
        if l > r:
            l, r = r, l
        LR.append([l, r])

    LIST = [0]
    for s in S:
        if s == "1":
            LIST.append(LIST[-1] + 1)

        else:
            LIST.append(LIST[-1])

    out_lines = []
    for l, r in LR:
        m = LIST[r] - LIST[l - 1]
        total_len = r - l + 1
        n_zero = total_len - m
        out_lines.append(str(count(m, n_zero, mod)))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main(10)
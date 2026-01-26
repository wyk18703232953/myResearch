def steps(start, target):
    ans = 0
    for i, v in enumerate(start):
        u = target[i]
        if v != u:
            for j in range(i + 1, len(start)):
                a, b = start[j], target[j]
                if a != b and a == u:
                    start[i], start[j] = start[j], start[i]
                    break
            ans += 1
    return ans


def solve(seq):
    hc = seq.count('H')
    tc = len(seq) - hc
    ans = float('inf')
    for i in range(tc + 1):
        s = ['T'] * i + ['H'] * hc + ['T'] * (tc - i)
        ans = min(steps(seq.copy(), s), ans)
    for i in range(hc + 1):
        s = ['H'] * i + ['T'] * tc + ['H'] * (hc - i)
        ans = min(steps(seq.copy(), s), ans)
    return ans


def main(n):
    if n < 0:
        n = 0
    # Deterministically generate a sequence of length n using a simple pattern
    # Pattern: position i is 'H' if i is even, else 'T'
    seq = ['H' if i % 2 == 0 else 'T' for i in range(n)]
    result = solve(seq)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)
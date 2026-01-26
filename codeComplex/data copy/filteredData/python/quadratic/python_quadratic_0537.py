#!/usr/bin/env python3

N = 55

# Precompute f exactly as in the original program
f = [0]
for i in range(1, N):
    f.append(f[-1] * 4 + 1)
    if f[-1] > 1e18:
        break


def solve_single(n, m):
    if n > 31:
        return "YES {}".format(n - 1)
    start = 0
    found = False
    res = -1
    for i in range(1, n + 1):
        start += 2 ** i - 1
        end = start
        for k in range(1, i + 1):
            end += f[n - k] * (2 ** (k + 1) - 3)
        if m >= start and m <= end:
            found = True
            res = i
            break
    if found:
        return "YES {}".format(n - res)

    else:
        return "NO"


def main(n):
    # n controls the number of test cases and the scale of (n, m) pairs.
    # Deterministic generation: for case index i (1-based),
    # let nn = (i % 40) + 1, mm = i * (i + 1) // 2.
    # This keeps nn in a reasonable range and grows mm with i.
    t = n if n > 0 else 1
    results = []
    for i in range(1, t + 1):
        nn = (i % 40) + 1
        mm = i * (i + 1) // 2
        results.append(solve_single(nn, mm))
    for line in results:
        # print(line)
        pass
if __name__ == "__main__":
    main(10)
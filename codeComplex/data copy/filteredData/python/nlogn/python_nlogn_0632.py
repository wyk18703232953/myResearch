import sys

def main(n):
    # n controls the size of the input:
    # let m = max(2, n//2), and total length of x,t is n + m (as in the original loop)
    if n < 3:
        n = 3
    m = max(2, n // 2)
    total_len = n + m

    # Deterministic generation of x and t
    # x: strictly increasing sequence to keep comparisons meaningful
    x = [i * 2 for i in range(total_len)]

    # t: first m positions are 1 (tx), remaining are 0 (p),
    # ensuring exactly m ones so that tx has length m
    t = [1] * m + [0] * n

    # Original logic from here
    if m == 1:
        # print(n)
        pass
        return

    p = []
    tx = []
    for i in range(n + m):
        (tx if t[i] == 1 else p).append(x[i])

    a = [0] * m
    i = 0
    for pi in p:
        while i < m - 1 and pi > (tx[i] + tx[i + 1]) / 2:
            i += 1
        a[i] += 1

    # print(" ".join(str(ai) for ai in a))
    pass
if __name__ == "__main__":
    main(10)
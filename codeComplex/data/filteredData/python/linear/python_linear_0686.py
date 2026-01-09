import sys
sys.setrecursionlimit(2000)
from collections import Counter

def main(n):
    # Deterministically generate b based on n
    # b has length n//2, as implied by original logic (accessing b[i+1] up to i=n//2-2)
    m = max(1, n // 2)
    b = [i * 2 + 1 for i in range(m)]  # simple deterministic increasing sequence

    l = 0
    r = b[0]
    a = [0] * n
    half = n // 2
    for i in range(half):
        a[i] = l
        a[n - 1 - i] = r
        if i != half - 1:
            val = b[i + 1]
            summ = l + r
            if summ == val:
                continue
            elif summ > val:
                diff = summ - val
                r -= diff

            else:
                diff = val - summ
                l += diff

    for x in a:
        # print(x, end=' ')
        pass
    # print('')
    pass
if __name__ == "__main__":
    main(10)
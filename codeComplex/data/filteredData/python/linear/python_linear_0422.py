import sys
from collections import Counter

def core_logic(n, x, a):
    d = Counter(a)
    sa = set(a)
    if len(sa) < n:
        return 0

    else:
        for i in a:
            k = i & x
            if k != i and k in d:
                return 1
        z = [i & x for i in a]
        if len(set(z)) < n:
            return 2

        else:
            return -1

def main(n):
    # Deterministic data generation
    # Interpret n as array length; x chosen deterministically from n
    x = (n // 2) ^ (n * 3 + 7)
    a = [ (i * 17 + 23) & ((1 << 20) - 1) for i in range(n) ]
    result = core_logic(n, x, a)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)
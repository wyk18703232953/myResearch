import atexit
import io
import sys

# Buffering IO (kept but unused for stdin; stdout still buffered deterministically)
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def main(n):
    # n controls the size of the input:
    # - we generate n pairs (x, k_x) but use a single k as the maximum of all k_x
    # - list p has length n
    # All values are generated deterministically from n and indices.
    if n <= 0:
        print()
        return

    # Deterministically generate k based on n
    # k is at least 1 to avoid division by zero or empty ranges
    k = max(1, n // 3)

    # Deterministically generate p as a list of positive integers
    # Values grow roughly linearly with n but include some variation
    p = [(i * 2 + (i // 3) + n) for i in range(1, n + 1)]

    t = []
    g = {}
    for x in p:
        if x in g:
            t.append(g[x])
            continue
        kk = x - 1
        while True:
            if kk in g:
                if x - g[kk] < k:
                    ttt = g[kk]
                else:
                    ttt = kk + 1
                for i in range(kk + 1, x + 1):
                    g[i] = ttt
                t.append(g[x])
                break
            elif kk < 0 or x - kk == k:
                for i in range(kk + 1, x + 1):
                    g[i] = kk + 1
                t.append(g[x])
                break
            kk -= 1

    print(' '.join(str(x) for x in t))


if __name__ == "__main__":
    # Example deterministic call; change n to scale the experiment
    main(10)
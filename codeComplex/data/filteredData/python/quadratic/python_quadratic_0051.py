import sys


class fenwick():
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)

    def to_sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= (i & -i)
        return s

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += (i & -i)

    def get(self, i, j):
        return self.to_sum(j) - self.to_sum(i-1)


def main(n):
    if n <= 0:
        return
    # permutation of size n: a simple deterministic pattern with inversions
    permutation = [((i * 2 + 1) % n) + 1 for i in range(n)]
    seq = [(permutation[i], i + 1) for i in range(n)]
    seq.sort(reverse=True)

    # number of queries scales with n
    m = n
    query = []
    for i in range(m):
        l = (i % n) + 1
        r = ((i * 3) % n) + 1
        if l > r:
            l, r = r, l
        query.append((l, r))

    WHOLE_INVERSION = 0
    fenwick_1 = fenwick(n)

    for value, index in seq:
        WHOLE_INVERSION += fenwick_1.get(1, index)
        fenwick_1.add(index, 1)

    out_lines = []
    for l, r in query:
        d = r - l + 1
        WHOLE_INVERSION += d*(d-1)//2
        if WHOLE_INVERSION % 2 != 0:
            out_lines.append("odd")

        else:
            out_lines.append("even")
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main(10)
import sys


class fenwick():
    """
    This Tree Data Structure speeds up calculating summations of partial sum 
    and also updating subsets of sequences. Both queries finish in logarithmic times.
    """
    # 1-indexed

    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)

    def to_sum(self, i):
        # return sigma(a_j) (0<=j<=i)
        s = 0
        while i > 0:
            s += self.data[i]
            i -= (i & -i)
        return s

    def add(self, i, x):
        # a_i -> a_i + x
        while i <= self.n:
            self.data[i] += x
            i += (i & -i)

    def get(self, i, j):
        # return sigma(a_k) (i<=k<=j)
        return self.to_sum(j) - self.to_sum(i - 1)


def main(n):
    # Construct permutation of size n deterministically: 1..n
    permutation = list(range(1, n + 1))
    seq = [(permutation[i], i + 1) for i in range(n)]
    seq.sort(reverse=True)

    # Let number of queries scale with n as n; each query is [1, n]
    m = n
    query = [(1, n) for _ in range(m)]

    # count whole inversion
    WHOLE_INVERSION = 0
    fenwick_1 = fenwick(n)

    for value, index in seq:
        WHOLE_INVERSION += fenwick_1.get(1, index)
        fenwick_1.add(index, 1)

    # process queries
    outputs = []
    for l, r in query:
        d = r - l + 1
        WHOLE_INVERSION += d * (d - 1) // 2
        if WHOLE_INVERSION % 2 != 0:
            outputs.append("odd")

        else:
            outputs.append("even")

    return outputs


if __name__ == "__main__":
    # example deterministic run
    result = main(5)
    for line in result:
        # print(line)
        pass
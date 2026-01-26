import math, functools, itertools, operator, bisect, fractions, statistics
from collections import deque, defaultdict, OrderedDict, Counter
from fractions import Fraction
from decimal import Decimal
from heapq import heappush, heappop, heapify, _heapify_max, _heappop_max, nsmallest, nlargest

def main(n):
    # n is the "input" to the original program
    # Original logic:
    #   read integer n
    #   find largest t such that t^2 <= n
    #   build array a using t as block size
    #
    # Here we use the provided n directly.
    ans = []
    i = 1
    k = 1
    t = 0
    while True:
        k = i * i
        if k <= n:
            t = i

        else:
            break
        i += 1

    a = []
    z = []
    for i in range(n):
        z += [i + 1]
        if len(z) == t:
            a = z + a
            z = []
    a = z + a

    # Return result instead of printing, so caller can measure time if needed
    return a

if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    result = main(10)
    # print(" ".join(str(x) for x in result))
    pass
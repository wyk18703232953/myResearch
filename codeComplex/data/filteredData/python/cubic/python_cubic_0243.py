import math
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
from decimal import Decimal
from fractions import Fraction
from types import GeneratorType

INF = float('inf')
mod = int(1e9) + 7


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)

        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)

                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


@bootstrap
def recur(r, g, b):
    if (r + g + b) == r or (r + g + b) == g or (r + g + b) == b:
        yield 0
        return
    if dp[r][g][b]:
        yield dp[r][g][b]
        return
    if r > 0 and g > 0:
        dp[r][g][b] = max(dp[r][g][b], R[r - 1] * G[g - 1] + (yield recur(r - 1, g - 1, b)))
    if r > 0 and b > 0:
        dp[r][g][b] = max(dp[r][g][b], R[r - 1] * B[b - 1] + (yield recur(r - 1, g, b - 1)))
    if b > 0 and g > 0:
        dp[r][g][b] = max(dp[r][g][b], B[b - 1] * G[g - 1] + (yield recur(r, g - 1, b - 1)))
    yield dp[r][g][b]


def generate_lengths(n):
    r = n
    g = n
    b = n
    return r, g, b


def generate_arrays(r, g, b):
    R = [i + 1 for i in range(r)]
    G = [2 * (i + 1) for i in range(g)]
    B = [3 * (i + 1) for i in range(b)]
    R.sort()
    G.sort()
    B.sort()
    return R, G, B


def main(n):
    global R, G, B, dp
    r, g, b = generate_lengths(n)
    R, G, B = generate_arrays(r, g, b)
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    ans = recur(r, g, b)
    # print(ans)
    pass
if __name__ == "__main__":
    main(3)
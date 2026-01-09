import math
from types import GeneratorType

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

def encode(row, col, n, m):
    return row * m + col

def main(n):
    # Interpret n as grid size and steps:
    # n >= 2 : n = grid size, k = n if even, else n-1
    # n < 2  : default small case
    if n < 2:
        rows = 2
        cols = 2
        k = 2

    else:
        rows = n
        cols = n
        k = n if n % 2 == 0 else n - 1
        if k <= 0:
            k = 2

    r = rows
    c = cols

    if k % 2 == 1:
        for _ in range(r):
            # print(' '.join(map(str, [-1] * c)))
            pass
        return

    total_nodes = r * c
    adj = [[] for _ in range(total_nodes)]

    # Deterministic horizontal edge weights
    for i in range(r):
        weights = [(i * c + j) % 7 + 1 for j in range(c - 1)]
        for j in range(c - 1):
            cur = encode(i, j, r, c)
            nex = encode(i, j + 1, r, c)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    # Deterministic vertical edge weights
    for i in range(r - 1):
        weights = [((i + 1) * c + j * 3) % 9 + 1 for j in range(c)]
        for j in range(c):
            cur = encode(i, j, r, c)
            nex = encode(i + 1, j, r, c)
            w = weights[j]
            adj[cur].append((nex, w))
            adj[nex].append((cur, w))

    half_k = k // 2
    dp_size = r * c * (half_k + 1)
    dp = [-1] * dp_size

    @bootstrap
    def solve(node, remain):
        if remain == 0:
            yield 0
        key = node + remain * r * c
        mem = dp[key]
        if mem != -1:
            yield mem
        result = []
        for x in adj[node]:
            result.append((yield solve(x[0], remain - 1)) + x[1])
        ans = min(result)
        dp[key] = ans
        yield ans

    for i in range(r):
        ans_row = []
        for j in range(c):
            node = encode(i, j, r, c)
            cost = solve(node, half_k) * 2
            ans_row.append(cost)
        # print(' '.join(map(str, ans_row)))
        pass
if __name__ == "__main__":
    main(5)
from collections import deque

def main(n):
    # Interpret n as both the length of S and the number of queries q
    q = n
    S = [i % 10 for i in range(1, n + 1)]

    Q = deque(S)
    n_q = len(Q)
    res = []
    for _ in range(n_q):
        a = Q.popleft()
        b = Q.popleft()
        Q.appendleft(max(a, b))
        Q.append(min(a, b))
        res.append((a, b))

    A = list(Q)

    def solve(t):
        if t < len(res):
            return res[t - 1]
        t -= len(res) + 1
        t %= n_q - 1
        return A[0], A[t + 1]

    # Deterministically generate q query times t
    # Use a simple pattern so that t covers small and larger values
    queries = [(i * 3 + 1) for i in range(1, q + 1)]

    out_lines = []
    for t in queries:
        x, y = solve(t)
        out_lines.append(f"{x} {y}")
    # print("\n".join(out_lines))
    pass
if __name__ == "__main__":
    main(10)
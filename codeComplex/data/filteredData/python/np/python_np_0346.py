from functools import lru_cache

P = 10**9 + 7

def build_input(n):
    # Interpret n as number of tasks N, and set total time T as sum of durations
    if n <= 0:
        N = 1
    else:
        N = n
    X = []
    T = 0
    for i in range(N):
        t = (i + 1)  # duration
        g = i % 3    # group
        X.append((t, g))
        T += t
    return N, T, X

def main(n):
    N, T, X_local = build_input(n)

    @lru_cache(maxsize=None)
    def calc(x, pr, t):
        if t < 0:
            return 0
        if t == 0:
            return 1
        if x == 0:
            return 0

        ans = 0
        for i in range(N):
            if x & (1 << i):
                if X_local[i][1] != pr:
                    y = x ^ (1 << i)
                    ans = (ans + calc(y, X_local[i][1], t - X_local[i][0])) % P
        return ans

    if N > 60:
        return 0

    return calc((1 << N) - 1, -1, T)

if __name__ == "__main__":
    print(main(5))
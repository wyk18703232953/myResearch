import sys
from functools import lru_cache

def generate_input(n):
    # n: number of tasks, total time T = n
    T = n
    S = []
    for i in range(n):
        duration = 1 + (i % 3)  # durations in {1,2,3}
        category = i % 4        # categories in {0,1,2,3}
        S.append([duration, category])
    return n, T, S

def main(n):
    n, T, S = generate_input(n)
    mod = 10**9 + 7

    @lru_cache(maxsize=None)
    def calc(used, recent, time):
        ANS = 0
        for i in range(n):
            if i in used:
                continue
            if time + S[i][0] > T:
                continue
            if S[i][1] == recent:
                continue
            if time + S[i][0] == T:
                ANS += 1
            if time + S[i][0] < T:
                used2 = list(used) + [i]
                used2.sort()
                recent2 = S[i][1]
                time2 = time + S[i][0]
                ANS = (ANS + calc(tuple(used2), recent2, time2)) % mod
        return ANS

    result = calc(tuple(), -1, 0) % mod
    print(result)
    return result

if __name__ == "__main__":
    main(10)
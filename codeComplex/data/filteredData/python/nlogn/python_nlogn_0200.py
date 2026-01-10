from collections import deque
import heapq


def main(n):
    # Deterministically generate T and problems based on n
    # Interpret n as number of problems
    T = n * n  # total allowed time grows quadratically with n
    problems = []
    for i in range(1, n + 1):
        a = (i % (n + 1)) + 1  # required number of problems solved before this, bounded
        t = (i * 2) % (n + 3) + 1  # time cost, bounded and deterministic
        problems.append((a, t))

    def possible(K):
        d = []
        for a, t in problems:
            if a >= K:
                d.append(t)
        d.sort()
        if len(d) < K:
            return False
        else:
            return sum(d[:K]) <= T

    l = 0
    r = n + 1
    while r - l > 1:
        med = (r + l) // 2
        if possible(med):
            l = med
        else:
            r = med

    print(l)
    print(l)
    d = []
    for i, (a, t) in enumerate(problems):
        if a >= l:
            d.append((t, i + 1))
    d.sort(key=lambda x: x[0])
    ans = [v[1] for v in d[:l]]
    if ans:
        print(*ans)
    else:
        print()


if __name__ == "__main__":
    main(10)
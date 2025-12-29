###############################
# Converted from:
# https://codeforces.com/contest/1010/problem/A
# Logic wrapped into main(n) with generated test data.
################################
import random
import math


def solve(m, up, down):
    n = len(up)

    def check(x):
        weight = m + x
        fuel = x
        for i in range(n):
            f = weight / up[i]
            if fuel < f:
                return False
            weight -= f
            fuel -= f

            f = weight / down[i]
            if fuel < f:
                return False
            weight -= f
            fuel -= f
        return True

    l = 0.0
    r = 1e9 + 1e-6

    for _ in range(100):
        mid = (l + r) / 2.0
        if check(mid):
            r = mid
        else:
            l = mid
        if r - l <= 1e-10:
            break

    if l >= 1e9 + 1e-6:
        return -1
    else:
        return l


def main(n):
    """
    n: problem size (number of stages).
    Generates random test data based on n and prints the answer
    using the same logic as the original solution.
    """
    # Generate test data:
    # m: base weight in [1, 1000]
    m = random.randint(1, 1000)
    # up[i], down[i] must be > 1 to avoid division issues; keep them small-ish.
    up = [random.randint(2, 20) for _ in range(n)]
    down = [random.randint(2, 20) for _ in range(n)]

    ans = solve(m, up, down)
    if ans == -1:
        print(-1)
    else:
        print(f"{ans:.10f}")


if __name__ == "__main__":
    # Example: run with n = 5
    main(5)
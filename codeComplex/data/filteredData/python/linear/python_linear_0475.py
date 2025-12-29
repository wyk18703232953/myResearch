import random
from collections import defaultdict

def solve_instance(n, c, a):
    # Original solve() logic, without input()
    c = [0] + c
    a = [0] + a
    vis = [False] * (n + 1)
    ans = 0

    d = defaultdict(lambda: 0)
    cycleno = 0

    for i in range(1, n + 1):
        if not vis[i]:
            cur = i
            while not vis[cur]:
                d[cur] = cycleno
                vis[cur] = True
                cur = a[cur]

            if d[cur] == cycleno:
                min_ = c[cur]
                first = cur
                cur = a[cur]
                while first != cur:
                    min_ = min(c[cur], min_)
                    cur = a[cur]
                ans += min_
            cycleno += 1

    return ans


def main(n):
    # Generate test data for given n
    # c[i] in [1, 1000], a is a random permutation of 1..n
    c = [random.randint(1, 1000) for _ in range(n)]

    # Generate a random permutation to form a mapping a[1..n]
    a = list(range(1, n + 1))
    random.shuffle(a)

    # Solve and print the answer
    ans = solve_instance(n, c, a)
    print(ans)


if __name__ == "__main__":
    # Example: run main with n = 10
    main(10)
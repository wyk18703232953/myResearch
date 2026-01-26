import math as mt
import itertools as it

def main(n):
    # n: number of problems
    if n <= 0:
        print(0)
        return

    l = n
    r = 2 * n
    x = max(1, n // 3)

    a = [i % 100 + 1 for i in range(1, n + 1)]

    ans = 0
    for j in range(2, n + 1):
        for comb in it.combinations(a, j):
            if max(comb) - min(comb) >= x and l <= sum(comb) <= r:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main(8)
def check(j, l, r, x):
    s = sum(j)
    if s >= l and s <= r and (max(j) - min(j)) >= x:
        return 1
    return 0

from itertools import combinations

def main(n):
    if n < 2:
        print(0)
        return

    # Deterministic parameter generation based on n
    l = n
    r = 2 * n
    x = max(1, n // 5)

    # Deterministic list c of length n
    c = [i * 2 + 1 for i in range(1, n + 1)]

    count = 0
    for i in range(2, n + 1):
        a = combinations(c, i)
        for j in a:
            if check(j, l, r, x):
                count += 1
    print(count)

if __name__ == "__main__":
    main(10)
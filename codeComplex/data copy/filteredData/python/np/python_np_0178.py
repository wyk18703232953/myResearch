from itertools import combinations

def main(n):
    # Deterministically generate parameters and array based on n
    l = n
    r = 3 * n
    x = max(1, n // 3)
    a = [(i * 2 + 1) % (2 * n + 1) + 1 for i in range(n)]

    count = 0
    for i in range(2, n + 1):
        for j in combinations(a, i):
            if max(j) - min(j) >= x and l <= sum(j) <= r:
                count += 1
    print(count)


if __name__ == "__main__":
    main(10)
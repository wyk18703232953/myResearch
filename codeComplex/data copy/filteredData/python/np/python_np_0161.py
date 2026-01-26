from itertools import combinations

def main(n):
    # Deterministically generate parameters based on n
    l = n // 3
    r = n // 2 + n
    x = max(1, n // 5)

    # Deterministically generate list a of length n
    # Values are simple arithmetic based on index and n
    a = [(i * 2 + n) % (2 * n + 3) + 1 for i in range(n)]

    # Core logic from original program
    count = sum(
        sum(
            max(j) - min(j) >= x and l <= sum(j) <= r
            for j in combinations(a, i)
        )
        for i in range(2, n + 1)
    )

    print(count)


if __name__ == "__main__":
    main(10)
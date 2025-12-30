import math
import random


def solve_naive(n, k):
    taken = set()
    current_cap = 0
    found = False
    while current_cap != n:
        for c in range(k, 1, -1):
            found = False
            if current_cap == 0:
                if c <= n:
                    current_cap += c
                    taken.add(c)
                    found = True
                    break
            else:
                if c not in taken and c - 1 <= n - current_cap:
                    current_cap += c - 1
                    taken.add(c)
                    found = True
                    break
        if not found:
            break
    return len(taken) if found else -1


def solve(n, k):
    if n == 1:
        return 0
    if k >= n:
        return 1
    else:
        disc = (3 - 2 * k) ** 2 - 8 * (n - k)
        if disc < 0:
            return -1
        t = (-math.sqrt(disc) + (2 * k) - 3) / 2
        if t == 0.0:
            return 2
        if t % 1 == 0:
            return 1 + int(t)
        else:
            return 2 + int(t)


def main(n):
    """
    n: problem scale, used here to generate test data (n, k).
       We generate one test (n_val, k_val) and print solve(n_val, k_val).

    Test data generation rule (can be adjusted as needed):
        1 <= n_val <= n
        1 <= k_val <= n
    """
    if n < 1:
        return

    # Generate a single test case (n_val, k_val) based on scale n
    n_val = random.randint(1, n)
    k_val = random.randint(1, n_val)  # typical constraint: k <= n

    # Run and print result
    print(solve(n_val, k_val))


if __name__ == "__main__":
    # Example: run with scale 10
    main(10)
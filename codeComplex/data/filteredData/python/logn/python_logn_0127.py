"""
Converted version of the Codeforces 287B solution.

Changes:
1. Removed input().
2. Added main(n) that encapsulates logic; n is the scale.
3. Test data is generated from n:
   - We create a list of pairs (n_i, k_i) and solve each.
"""

def sum_upto(num: int) -> int:
    # sum of 1..num
    return (num * (num + 1)) // 2


def sum_from_to(fromm: int, to: int) -> int:
    if fromm <= 1:
        return sum_upto(to)
    # sum from fromm..to
    return sum_upto(to) - sum_upto(fromm - 1)


def min_splitters(n: int, k: int) -> int:
    start = 1
    end = k
    while start < end:
        mid = (start + end) // 2
        mid_val = sum_from_to(mid, k)
        if mid_val == n:
            return k - mid + 1
        elif mid_val > n:
            start = mid + 1
        else:
            end = mid
    return k - start + 1


def solve_single_case(n: int, k: int) -> int:
    # original logic wrapped for a single (n, k) instance
    if n == 1:
        return 0
    elif n <= k:
        return 1
    else:
        k -= 1
        n -= 1
        if sum_upto(k) < n:
            return -1
        return min_splitters(n, k)


def generate_test_data(n: int):
    """
    Generate a list of (n_i, k_i) pairs based on the scale n.
    Here we build some varying test pairs:
      - small k
      - medium k
      - large k up to n
    This is arbitrary and only for demonstration.
    """
    tests = []
    if n <= 0:
        return tests

    # ensure at least one test
    tests.append((max(1, n // 2), max(1, n // 3)))

    # some additional tests
    tests.append((n, max(1, n // 2)))
    tests.append((max(2, n - 1), max(1, n - 1)))
    tests.append((max(3, n // 3), max(2, n // 2)))

    # deduplicate
    tests = list(dict.fromkeys(tests))
    return tests


def main(n: int):
    """
    n is the scale parameter.
    This main generates test data based on n and prints answers
    for each (n_i, k_i) pair.
    """
    test_cases = generate_test_data(n)
    for ni, ki in test_cases:
        ans = solve_single_case(ni, ki)
        print(ni, ki, ans)


if __name__ == "__main__":
    # example: run main with some scale, e.g. 10
    main(10)
from bisect import bisect_right
import random

MOD = 10**9 + 7

def solve(n, x, y, intervals):
    # intervals: list of (s, e), length n
    s = [0] * n
    e = [0] * n
    v = [0] * n
    c = 0

    for i in range(n):
        s[i], e[i] = intervals[i]
        c += x + (e[i] - s[i]) * y

    s.sort()
    e.sort()

    for i in range(n - 2, -1, -1):
        k = bisect_right(s, e[i])
        while k < n and v[k] == 1 and (s[k] - e[i]) * y < x:
            k += 1
        if k == n:
            continue
        if (s[k] - e[i]) * y < x:
            v[k] = 1
            c += (s[k] - e[i]) * y - x

    return c % MOD


def generate_test_data(n):
    # Generate parameters x, y
    # Ensure positive, and y not too large to avoid overflow in typical ranges
    x = random.randint(1, 10**6)
    y = random.randint(1, 10**6)

    intervals = []
    current = 0
    for _ in range(n):
        # generate non-negative, increasing-ish intervals
        start = current + random.randint(0, 10)
        end = start + random.randint(1, 10)
        intervals.append((start, end))
        # occasionally reset to allow overlaps
        if random.random() < 0.3:
            current = random.randint(0, current + 5)
        else:
            current = end

    return x, y, intervals


def main(n):
    x, y, intervals = generate_test_data(n)
    result = solve(n, x, y, intervals)
    print(result)


if __name__ == "__main__":
    # example: run with some default n
    main(5)
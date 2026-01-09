def f(n, t, data_iter):
    a = 0
    f_val = 1
    for _ in range(n):
        for x in data_iter:
            if x != f_val:
                a += 1
            f_val = 1 - f_val
    if t < 3:
        for _ in data_iter:
            pass
    return a

def main(n):
    # Deterministic data generation to replace interactive inputs
    # Original program structure:
    #   n = int(input())
    #   then for each i in range(4): m.append(f(n, i))
    # Each f(n, t) consumed from rd(), which read digits from input() one-by-one.
    #
    # We emulate this by:
    # - Creating a flat sequence of integers that would come from input
    # - Slicing it deterministically per call so total consumption pattern
    #   is independent of t for time-complexity experiments.

    from itertools import permutations as p

    # Define a base sequence of "digit-like" integers (0 or 1) deterministically
    # Its length must be large enough to cover all consumption in worst case.
    # Each call to f(n, t) uses:
    #   - main loop: n lines, each with some count; we approximate with 2*n
    #   - plus an extra line when t < 3
    # Here we just allocate 6*n elements per call to comfortably exceed usage.
    per_call_len = 6 * n
    total_len = 4 * per_call_len
    base_data = [(i // 2) % 2 for i in range(total_len)]

    m = []
    for i in range(4):
        start = i * per_call_len
        end = start + per_call_len
        data_slice = base_data[start:end]
        m.append(f(n, i, data_slice))

    b = [-1, -1, 1, 1]
    res = 2 * n ** 2 + min(
        sum(x * y for x, y in zip(q, m)) for q in set(p(b))
    )
    # print(res)
    pass
if __name__ == "__main__":
    main(10)
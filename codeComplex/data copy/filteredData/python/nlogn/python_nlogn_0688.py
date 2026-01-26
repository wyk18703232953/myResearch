def main(n):
    # Interpret n as the size of arrays a and b
    if n < 2:
        n = 2  # ensure at least two elements for a[-2]

    # Deterministic generation of a and b
    # a will be sorted automatically since it's increasing
    a = [i for i in range(1, n + 1)]
    # b constructed to have values relative to a for varied conditions
    # Here we choose b so that often max(a) < min(b) holds when n is large
    b = [n + 1 + (i % 3) for i in range(n)]

    m = len(b)

    a_sorted = sorted(a)
    max_a = a_sorted[-1]
    min_b = min(b)

    if max_a < min_b:
        result = sum(a_sorted) * m + sum(b) - a_sorted[-1] * (m - 1) - a_sorted[-2]
    elif max_a == min_b:
        result = sum(a_sorted) * m + sum(b) - a_sorted[-1] * m

    else:
        result = -1

    # print(result)
    pass
if __name__ == "__main__":
    main(10)
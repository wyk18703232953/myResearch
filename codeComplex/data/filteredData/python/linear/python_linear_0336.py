def main(n):
    # In the original problem:
    # n = number of elements in the list
    # k = given integer
    # l = list of positions (sorted)
    #
    # Here we map the experimental scale n to:
    # - length of l: n
    # - k: a fixed positive integer (e.g., 3)
    #
    # We generate a deterministic, increasing sequence l of length n.

    if n <= 0:
        return 0

    k = 3
    # Deterministic, strictly increasing sequence
    l = [i * 2 for i in range(n)]

    o = 2
    for i in range(n):
        if i + 1 == n:
            break

        d = abs(l[i] - l[i + 1]) / k
        if d == 2:
            o += 1
        elif d > 2:
            o += 2

    return o


if __name__ == "__main__":
    # Example deterministic call for demonstration
    result = main(10)
    print(result)
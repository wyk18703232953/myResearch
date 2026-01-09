def main(n):
    import math

    # Deterministic data generation
    # Interpret n as the number of points; set d as a simple function of n
    if n <= 0:
        return 0

    d = n // 3 + 1  # ensure d >= 1

    # Generate strictly increasing positions with controlled gaps
    # Gaps follow a simple deterministic pattern depending on d
    pos = []
    current = 0
    for i in range(n):
        gap = (i % (2 * d + 1)) + 1
        current += gap
        pos.append(current)

    count = 2
    for i in range(1, n):
        if math.fabs(pos[i] - pos[i - 1]) > 2 * d:
            count += 2
        elif math.fabs(pos[i] - pos[i - 1]) == 2 * d:
            count += 1

        else:
            continue

    # For timing experiments, return the result instead of printing
    return count


if __name__ == "__main__":
    # Example deterministic call for benchmarking
    result = main(10)
    # print(result)
    pass
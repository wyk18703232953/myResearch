def main(n):
    import math

    # Map n to problem parameters deterministically
    # Number of elements in z
    m = max(1, n)
    # Generate z as [1, 2, ..., m]
    z = [i + 1 for i in range(m)]
    # Set l, r, x based on n in a deterministic way
    # Ensure ranges are reasonable relative to sum of z
    total_sum = m * (m + 1) // 2
    x = max(1, n // 3)
    l = total_sum // 4
    r = total_sum // 2

    count = 0
    for i in range(pow(2, len(z))):
        mini = math.inf
        maxa = 0
        j = i
        inde = 0
        sume = 0
        while j > 0:
            if j & 1:
                sume += z[inde]
                maxa = max(maxa, z[inde])
                mini = min(mini, z[inde])
            j = j >> 1
            inde += 1
        if maxa != 0 and maxa - mini >= x and l <= sume <= r:
            count += 1

    print(count)


if __name__ == "__main__":
    main(10)
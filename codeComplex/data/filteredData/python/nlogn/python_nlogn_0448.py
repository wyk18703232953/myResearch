def main(n):
    # Interpret n as length of numbers array
    # Deterministically generate m and numbers
    if n <= 0:
        print(0)
        return

    m = n // 2  # median-like value
    numbers = [(i * 2 + 3) % (n + 3) for i in range(n)]
    if m not in numbers:
        # Ensure m exists in numbers deterministically by overwriting one position
        pos = n // 3
        numbers[pos] = m

    smaller_greater = [(0, 0)]
    for k in numbers:
        s, g = smaller_greater[-1]
        if k < m:
            smaller_greater.append((s + 1, g))
        elif k > m:
            smaller_greater.append((s, g + 1))
        else:
            smaller_greater.append((s, g))

    i = numbers.index(m)
    s_median, g_median = smaller_greater[i]

    difference = {}
    for pack in smaller_greater[i + 1:]:
        s, g = pack
        s -= s_median
        g -= g_median
        diff = s - g
        if diff in difference:
            difference[diff] += 1
        else:
            difference[diff] = 1

    count = 0
    for start in range(i + 1):
        s, g = smaller_greater[start]
        s -= s_median
        g -= g_median
        d1 = s - g
        d2 = d1 - 1
        if d1 in difference:
            count += difference[d1]
        if d2 in difference:
            count += difference[d2]

    print(count)


if __name__ == "__main__":
    main(10)
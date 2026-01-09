def main(n):
    # Ensure n is positive
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministic generation of a and b based on n
    # Pattern: a[i] and b[i] are chosen from '0' and '1' in a structured way
    a = [('0' if (i % 3 == 0 or i % 3 == 1) else '1') for i in range(n)]
    b = [('0' if (i % 3 == 0) else '1') for i in range(n)]

    count = 0
    skip_next = False
    for idx in range(n - 1):
        if skip_next:
            skip_next = False
            continue
        if a[idx] != b[idx] and a[idx] == b[idx + 1] and a[idx + 1] == b[idx]:
            count += 1
            a[idx] = b[idx]
            a[idx + 1] = b[idx + 1]
            skip_next = True

    for idx in range(n):
        if a[idx] != b[idx]:
            count += 1

    # print(count)
    pass
if __name__ == "__main__":
    main(10)
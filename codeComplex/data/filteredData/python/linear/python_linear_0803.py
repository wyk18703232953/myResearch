def main(n):
    # Interpret n as the length of array a and also as a[0] upper bound scale
    # Deterministically generate input structure:
    # n_list: [n0, n1, k] where n1 = length of a, k > 0
    n0 = n
    n1 = n
    k = max(1, n // 3)  # ensure k >= 1
    n_list = [n0, n1, k]

    # Generate a: non-decreasing sequence of integers of length n1
    # Example pattern: a[i] = (i * (i // 2 + 1)) % (5 * n1 + 7)
    # Then sort to mimic typical input characteristics
    a = [(i * (i // 2 + 1)) % (5 * n1 + 7) for i in range(n1)]
    a.sort()

    # Core logic from original program
    k = n_list[2]
    ans = 0
    dele = 1
    i = 0
    while i < n_list[1]:
        count = 1
        while (i + count) < n_list[1] and (a[i + count] - dele) // k == (a[i] - dele) // k:
            count += 1
        ans += 1
        dele += count
        i += count

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
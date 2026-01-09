def main(n):
    # Deterministic generation of n, m, k and mi
    # Interpret n as the length of mi
    if n <= 0:
        return

    # Set m and k deterministically based on n
    m = 2 * n
    k = max(1, n // 3)

    # Generate mi as a sorted list of positions within [1, m]
    # Use a simple arithmetic pattern to ensure determinism
    mi = []
    for i in range(1, n + 1):
        val = (i * 2 + (i // 3)) % m + 1
        mi.append(val)
    mi.sort()

    ans = 0
    items_to_del = 0
    shift = 1
    c_page = None
    for el in mi:
        if c_page is None:
            c_page = (el - shift) // k
            items_to_del = 1

        else:
            page = (el - shift) // k
            if page != c_page:
                shift += items_to_del
                ans += 1
                c_page = (el - shift) // k
                items_to_del = 1

            else:
                items_to_del += 1
    if items_to_del != 0:
        ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
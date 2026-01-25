def main(n):
    # n controls the size of the input list mi
    # Generate deterministic parameters
    if n <= 0:
        n = 1
    k = 5
    m = n
    # Generate a deterministic, strictly increasing list mi of size m
    # Values are spaced so that pages change regularly for experimentation
    mi = [i * 3 + 1 for i in range(1, m + 1)]

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
    print(ans)


if __name__ == "__main__":
    main(10)
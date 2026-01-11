def main(n):
    # Generate deterministic test data of size n
    # Each element is a tuple (l, r, original_index)
    # Ensure variety but fully deterministic using arithmetic patterns
    src = []
    for i in range(n):
        l = i // 2
        r = l + (i % 3) + 1
        src.append((l, r, i))

    src.sort()

    prev_l = 0
    max_r = 0
    prev_i = -1
    outer = -1

    for l, r, i in src:
        if prev_l == l:
            # print(prev_i + 1, i + 1)
            pass
            return
        if r <= max_r:
            # print(i + 1, outer + 1)
            pass
            return

        else:
            max_r = r
            outer = i
        prev_l = l
        prev_i = i
    # print(-1, -1)
    pass
if __name__ == "__main__":
    main(10)
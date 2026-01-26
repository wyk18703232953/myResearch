def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministic generation of a and b based on n
    # a: alternating '0' and '1'
    a = [str(i % 2) for i in range(n)]
    # b: a shifted by 1 with wrap-around
    b = [a[(i + 1) % n] for i in range(n)]

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
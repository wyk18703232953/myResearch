def main(n):
    from collections import defaultdict as dd

    # Deterministic construction of m and arr based on n
    # m will be a value that appears in arr and is around the middle
    m = (n // 3) % max(1, n) + 1  # ensure m >= 1

    # Construct arr of length n, with values around m and some >, <, ==
    arr = []
    for i in range(n):
        if i % 3 == 0:
            val = m
        elif i % 3 == 1:
            val = m + (i % 5) + 1
        else:
            val = max(1, m - (i % 5) - 1)
        arr.append(val)

    d = dd(int)
    has = False
    count = 0
    d[0] = 1
    total = 0

    for i in range(n):
        if arr[i] > m:
            count += 1
        if arr[i] < m:
            count -= 1
        if arr[i] == m:
            has = True
        if has:
            total += d[count] + d[count - 1]
        else:
            d[count] += 1

    print(total)


if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)
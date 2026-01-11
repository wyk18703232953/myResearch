def main(n):
    # Interpret n as the size of the array a; choose k deterministically as n//2 (at least 1)
    if n <= 0:
        return
    k = max(1, n // 2)

    # Deterministically generate array a of length n
    # Pattern: a[i] = (i * 3) % (n + 7) + i // 3
    a = [(i * 3) % (n + 7) + i // 3 for i in range(n)]

    mark, b = [], []
    for x in a:
        b.append(x)
        mark.append(False)
    b.sort(reverse=True)

    idx, profit = 0, 0
    while idx < k and idx < len(b):
        profit += b[idx]
        for i in range(n):
            if not mark[i] and a[i] == b[idx]:
                mark[i] = True
                break
        idx += 1
    # print(profit)
    pass

    prev, counter = -1, 0
    for i in range(n):
        if counter == (k - 1):
            break
        if mark[i]:
            # print(i - prev, end=' ')
            pass
            prev = i
            counter += 1
    # print(n - prev - 1)
    pass
if __name__ == "__main__":
    main(10)
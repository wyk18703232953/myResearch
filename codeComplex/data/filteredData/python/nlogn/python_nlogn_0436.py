def main(n):
    # n: length of the array
    # Deterministically generate array 'arr' of length n
    # Example pattern: arr[i] = (i * 3) % (2 * n + 1)
    if n <= 0:
        # print(0)
        pass
        return

    arr = [(i * 3) % (2 * n + 1) for i in range(n)]

    # Precompute powers of 2 up to 10**18
    k = []
    i = 0
    while 2 ** i <= 10 ** 18:
        k.append(2 ** i)
        i += 1

    # Count occurrences
    d = {}
    s1 = set()
    for i in arr:
        s1.add(i)
        if i not in d:
            d[i] = 1

        else:
            d[i] += 1

    s2 = set()
    for i in s1:
        flag = False
        for j in k:
            x = j - i
            y = d.get(x, -1)
            if y != -1:
                if x == i and d[i] == 1:
                    continue
                flag = True
                break
        if flag is False:
            s2.add(i)

    res = 0
    for i in s2:
        res += d[i]
    # print(res)
    pass
if __name__ == "__main__":
    # Example call; adjust n for different input scales
    main(10)
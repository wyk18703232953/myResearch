def main(n):
    # n: length of array
    if n <= 0:
        return

    # Deterministically define k based on n, with 1 <= k <= n
    k = max(1, n // 3)
    if k > n:
        k = n

    # Deterministically generate array of length n
    # Example: arr[i] = (i * 7) % 1000003
    arr = [(i * 7) % 1000003 for i in range(n)]

    new = []
    ans = 0
    for i in range(n):
        new.append((arr[i], i))
    new.sort(reverse=True)
    check = [0] * n
    for i in range(k):
        ans += new[i][0]
        check[new[i][1]] = 1
    count = 0
    res = []
    for i in range(n):
        if check[i] == 1:
            count += 1
            res.append(count)
            count = 0
        else:
            count += 1
    if res:
        res[-1] += count
    else:
        res.append(count)

    print(ans)
    print(*res)


if __name__ == "__main__":
    main(10)
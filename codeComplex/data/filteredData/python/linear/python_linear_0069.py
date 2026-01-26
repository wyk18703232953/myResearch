def main(n):
    # n: number of pairs (a, b)
    # deterministic data generation based on n
    s = n  # base value derived from n
    lst = []
    for i in range(n):
        # a decreases with i, b varies with i in a deterministic way
        a = n * 2 - i
        b = (i * 3) // 2 + (n % 5)
        lst.append([a, b])

    lst = sorted(lst, key=lambda x: x[0], reverse=True)
    prev, ans = s, 0
    for i in range(n):
        ans += prev - lst[i][0]
        if ans < lst[i][1]:
            ans += (lst[i][1] - ans)
        prev = lst[i][0]
    result = ans + prev
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)
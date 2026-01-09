def main(n):
    # n: number of pairs
    # Deterministically generate s and lst
    s = n * 2 + 5
    lst = [[i, (i * i) % (2 * n + 3) + 1] for i in range(n, 0, -1)]

    # Core logic from original code
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
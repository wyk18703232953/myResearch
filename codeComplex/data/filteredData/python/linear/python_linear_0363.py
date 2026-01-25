def main(n):
    # Interpret n as the length of price and bill lists
    if n <= 0:
        print(0)
        return

    # Deterministically generate prices c and bills a, both length n
    # Prices: descending pattern starting from n, not below 1
    c = [max(1, (n - i) // 2 + 1) for i in range(n)]
    # Bills: ascending pattern relative to index
    a = [(i * 3) // 2 + 1 for i in range(n)]

    ans = 0
    i = 0
    for bill in a:
        try:
            i += next(ind for ind, el in enumerate(c[i:]) if el <= bill) + 1
            ans += 1
        except StopIteration:
            break

    print(ans)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)
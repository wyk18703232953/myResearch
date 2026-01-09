def main(n):
    # Determine sizes for m and n based on input scale n
    # Here: number of games = n, number of bills = n
    games_count = n
    bills_count = n

    # Deterministic generation of prices c and bills a
    # c: game prices increasing with small variations
    c = [(i % 7) + (i // 3) for i in range(games_count)]
    # a: bills with values allowing some purchases
    a = [(i % 10) + (i // 2) for i in range(bills_count)]

    ans = 0
    i = 0
    for bill in a:
        try:
            i += next(ind for ind, el in enumerate(c[i:]) if el <= bill) + 1
            ans += 1
        except StopIteration:
            break

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
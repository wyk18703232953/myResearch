def main(n):
    # n: number of coins
    # Deterministic coin generation: descending sequence from n to 1
    coins = list(range(n, 0, -1))
    coins.sort(reverse=True)
    target = (sum(coins) + 2) // 2

    count = 1
    total = coins[count - 1]
    while total < target and count < len(coins):
        count += 1
        total += coins[count - 1]

    # print(count)
    pass
if __name__ == "__main__":
    main(10)
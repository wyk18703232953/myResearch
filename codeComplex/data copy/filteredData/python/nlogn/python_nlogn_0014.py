def main(n):
    # Interpret n as the number of houses N
    N = max(1, n)

    # Deterministically generate T based on N
    T = N // 2

    # Deterministically generate houses: list of (position, width)
    # Positions increase with i, widths vary deterministically with i
    houses = [(i * 3, (i % 5) + 1) for i in range(N)]

    houses.sort()

    count = 2  # borders left and right

    for (a, x), (b, y) in zip(houses, houses[1:]):
        gap = b - a - (x / 2 + y / 2)
        if gap > T:
            count += 2
        elif gap == T:
            count += 1

    # print(count)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)
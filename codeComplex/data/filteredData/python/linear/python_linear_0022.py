def main(n):
    # Generate deterministic input data based on n
    # a: single integer, here we set it as length of b for consistency
    a = n

    # Generate list b of length a with a controlled parity pattern
    # Ensure at least one even and one odd to match original logic
    if a == 0:
        b = []
    elif a == 1:
        # Single element, make it even
        b = [2]

    else:
        # For a >= 2, create a pattern with exactly one number of different parity
        # If a is even: all odd except last even -> one even
        # If a is odd: all even except last odd -> one odd
        if a % 2 == 0:
            b = [2 * i + 1 for i in range(a - 1)] + [2 * a]

        else:
            b = [2 * i for i in range(a - 1)] + [2 * a + 1]

    c = [int(i % 2 == 0) for i in b]
    if c.count(1) == 1:
        # print(c.index(1) + 1)
        pass

    else:
        # print(c.index(0) + 1)
        pass
if __name__ == "__main__":
    main(10)
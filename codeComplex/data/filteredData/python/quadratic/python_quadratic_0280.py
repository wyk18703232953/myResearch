def main(n):
    # Interpret n as both the size of list a and list b
    m = n

    # Deterministically generate a and b based on n
    # a: 0, 1, 2, ..., n-1
    a = list(range(n))
    # b: i % (n//2 + 1) to ensure some overlap; handle n=0 separately
    if n == 0:
        b = []
    else:
        base = n // 2 + 1
        b = [(i % base) for i in range(m)]

    # Core logic: print elements of a that are in b
    # Keep the same behavior of printing in one line separated by space
    result = []
    for x in a:
        if x in b:
            result.append(str(x))
    if result:
        print(" ".join(result))


if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)
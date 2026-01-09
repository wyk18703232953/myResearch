def main(n):
    # Interpret n as the length of each list
    m = n

    # Deterministic data generation
    l1 = [i for i in range(1, n + 1)]
    l2 = [i for i in range(n // 2 + 1, n + n // 2 + 1)]

    # Core logic preserved
    for i in l1:
        if i in l2:
            # print(i, end=" ")
            pass
if __name__ == "__main__":
    main(10)
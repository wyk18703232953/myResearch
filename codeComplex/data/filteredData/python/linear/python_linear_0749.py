def main(n):
    wyn = 1
    x = 4
    for _ in range(max(0, n - 1)):
        wyn += x
        x += 4
    print(wyn)


if __name__ == "__main__":
    # example deterministic call
    main(10)
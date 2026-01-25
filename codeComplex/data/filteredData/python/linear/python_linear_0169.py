def main(n):
    # n is the input scale
    if n < 6:
        print(-1)
    else:
        print(1, 2)
        print(1, 3)
        print(1, 4)
        for i in range(4, n):
            print(2, i + 1)

    for i in range(n - 1):
        print(1, i + 2)


if __name__ == "__main__":
    # example deterministic call; adjust n as needed for experiments
    main(10)
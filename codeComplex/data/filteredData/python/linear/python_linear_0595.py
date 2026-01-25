def main(n):
    total = 0
    for i in range(2, n + 1):
        j = 2
        while j * i <= n:
            total += i
            j += 1
    print(4 * total)


if __name__ == "__main__":
    main(1000)
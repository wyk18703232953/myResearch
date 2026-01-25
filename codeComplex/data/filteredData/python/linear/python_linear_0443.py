def main(n):
    ans = []
    m = int(n ** 0.5)
    x = n
    while x - m > 0:
        for i in range(1, m + 1):
            ans.append(x - m + i)
        x -= m
    for i in range(1, x + 1):
        ans.append(i)
    print(*ans)


if __name__ == "__main__":
    main(1000)
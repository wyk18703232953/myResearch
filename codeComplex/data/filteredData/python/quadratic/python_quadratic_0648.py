def main(n):
    # Generate deterministic data of size n
    # Example pattern: data[i] = (i % 7) + 1 to ensure small divisors and repeats
    data = [(i % 7) + 1 for i in range(n)]
    data.sort()
    ans = [0] * n
    col = 0
    for i in range(n):
        if ans[i] == 0:
            col += 1
            ans[i] = 1
            d = data[i]
            for j in range(i + 1, n):
                if data[j] % d == 0:
                    ans[j] = 1
    # print(col)
    pass
if __name__ == "__main__":
    main(10)
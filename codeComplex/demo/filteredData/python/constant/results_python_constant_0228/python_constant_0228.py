def main(n):
    a = n
    b = 2 * n + 1
    x = n // 2
    y = 3 * n
    z = n // 3
    ans = max(0, 2 * x + y - a) + max(0, 3 * z + y - b)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
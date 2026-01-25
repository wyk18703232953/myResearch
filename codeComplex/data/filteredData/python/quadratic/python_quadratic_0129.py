def main(n):
    # 将 n 视为数组长度，数值范围为 1..n
    a = n
    arr = [(i % a) + 1 for i in range(n)]
    mn = float("inf")
    for i in range(1, a + 1):
        mn = min(mn, arr.count(i))
    print(mn)


if __name__ == "__main__":
    main(10)
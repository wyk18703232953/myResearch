def main(n):
    if n <= 10:
        for i in range(n):
            # print(0, i)
            pass
        return
    # print(0, 0)
    pass
    for i in range(4, n + 1, 3):
        k = (i // 3) * 2
        # print(k, 0)
        pass
        # print(k - 1, 1)
        pass
        # print(k - 2, 2)
        pass
    k = ((n + 1) // 3) * 2
    if n % 3 == 0:
        # print(k - 1, 1)
        pass
        # print(k - 2, 2)
        pass
    elif n % 3 == 2:
        # print(k - 2, 2)
        pass
if __name__ == "__main__":
    main(10)
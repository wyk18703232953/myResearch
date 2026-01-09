def main(n):
    # n controls the size of the input array a; we keep 14 positions as in original
    # and deterministically generate values based on n
    length = 14
    a = [(i + 1) * n for i in range(length)]

    ans = 0
    for i in range(length):
        b = a.copy()
        b[i] = 0

        for j in range(1, length + 1):
            b[(i + j) % length] += (a[i] - 1) // length + ((a[i] - 1) % length + 1 > j - 1)

        current = 0
        for el in b:
            if el % 2 == 0:
                current += el
        if current > ans:
            ans = current

    return ans


if __name__ == "__main__":
    # example call; adjust n for different input scales
    # print(main(10))
    pass
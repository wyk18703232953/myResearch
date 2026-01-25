import math


def main(n):
    if n <= 0:
        return

    if n == 1:
        print(1)
        return

    if n == 2:
        print(1, 2)
        return

    if n == 3:
        print(1, 1, 3)
        return

    ar = [0] * 30

    for i in range(30):
        ar[i] = n // (2 ** i) - n // (2 ** (i + 1))

    sd = 0
    for i in range(30):
        if sd == n - 1:
            if n == (2 ** i):
                print(2 ** i)
            else:
                print(n - n % (2 ** (i - 1)))
            return
        for _ in range(ar[i]):
            print(2 ** i, end=' ')
            sd += 1


if __name__ == "__main__":
    # 示例：使用 n=100 作为规模参数
    main(100)
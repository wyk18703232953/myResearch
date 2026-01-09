import math


def main(n):
    x = n // 3 + 1
    y = (2 * n) // 3 + 1
    d1 = abs(1 - x) + abs(1 - y)
    d2 = abs(n - x) + abs(n - y)
    if d1 <= d2:
        # print('White')
        pass

    else:
        # print('Black')
        pass
if __name__ == "__main__":
    main(10)
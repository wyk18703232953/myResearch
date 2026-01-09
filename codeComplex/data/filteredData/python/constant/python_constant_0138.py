def main(n):
    # 将 n 映射为一对整数 (a, b)
    # 保证 b != 0
    a = n
    b = n // 2 + 1

    res = 0
    temp = 0

    if a % b == 0:
        # print(int(a / b))
        pass

    else:
        while b != 0:
            res += a // b
            a %= b
            temp = a
            a = b
            b = temp
        # print(res)
        pass
if __name__ == "__main__":
    main(10)
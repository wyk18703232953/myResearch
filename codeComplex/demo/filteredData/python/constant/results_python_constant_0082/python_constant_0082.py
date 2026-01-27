def Solve(n):
    if n <= 2:
        return n
    elif n % 6 == 0:
        return (n - 1) * (n - 2) * (n - 3)
    elif n % 2 == 0:
        return n * (n - 1) * (n - 3)

    else:
        return n * (n - 1) * (n - 2)


def main(n):
    # 在这里将 n 直接视为原问题中的输入规模
    result = Solve(n)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)
def main(n):
    # 映射：n 作为两个数的最大值范围
    # 构造确定性输入 a, b
    a = n
    b = n // 2

    x = a ^ b
    ans = 1
    while x > 0:
        x //= 2
        ans *= 2

    # print(ans - 1)
    pass
if __name__ == "__main__":
    main(10)
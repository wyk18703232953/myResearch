def main(n):
    # 生成输入：单个整数，规模由 n 决定
    # 这里构造一个既可能为正、也可能为负、也可能为小数位有限的整数
    x = n * (-1) ** (n % 3)  # 在正负之间变化，并保证确定性
    s = str(x)

    # 原始逻辑开始
    if int(s) > 0:
        result = s
    elif -9 <= int(s) <= 0:
        result = "0"

    else:
        a = (-int(s)) // 10
        b = ((-int(s)) // 100) * 10 + int(s[-1])
        result = str(max(-a, -b))

    # print(result)
    pass
if __name__ == "__main__":
    main(1000)
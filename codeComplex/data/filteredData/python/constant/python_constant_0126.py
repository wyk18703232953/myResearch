def main(n):
    # 确定性生成输入字符串 s
    # 映射规则：
    # - n 为偶数：正数字符串
    # - n 为奇数：负数字符串（以 - 开头）
    # - 数值部分为 n 的平方
    if n % 2 == 0:
        s = str(n * n)

    else:
        s = "-" + str(n * n)

    if int(s) < 0:
        k = int(s) / 10
        m = s[:len(s) - 2] + s[-1]
        # print(max(int(k), int(m)))
        pass

    else:
        # print(s)
        pass
if __name__ == "__main__":
    main(10)
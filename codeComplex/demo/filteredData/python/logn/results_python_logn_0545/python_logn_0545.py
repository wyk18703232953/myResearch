def main(n: int):
    # 生成测试数据：这里直接使用 n 作为原程序中的 k
    k = n

    s = k
    i = 1
    number_digits = 1
    while s - (i * (9 * 10 ** (i - 1))) > 0:
        number_digits = number_digits + 1
        s = s - (i * (9 * 10 ** (i - 1)))
        i += 1

    v = (s - 1) // number_digits
    s = s - v * number_digits
    ans = 10 ** (number_digits - 1) + v
    ans = str(ans)
    fans = ans[s - 1]
    # print(fans)
    pass
if __name__ == "__main__":
    # 示例：可以在此处修改 n 来做简单测试
    main(15)
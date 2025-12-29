def main(n):
    # 使用 n 作为“第 n 位数字”的规模（对应原代码中的 k+1）
    k = n - 1

    l = 1
    c = 9
    # 找到第 n 位数字所在的数字长度区间
    while k >= c * l:
        k -= c * l
        l += 1
        c *= 10

    # 确定具体的数字
    c = 10 ** (l - 1) + k // l
    # 输出该数字中的对应位
    print(str(c)[k % l])


# 示例：可根据需要修改测试规模 n
if __name__ == "__main__":
    test_n = 15  # 例如第 15 位数字
    main(test_n)
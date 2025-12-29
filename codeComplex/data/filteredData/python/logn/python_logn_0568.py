def main(n):
    import sys

    ind = 0
    dig = 0
    # 找到位数区间
    for i in range(1, 12):
        dig += i * 10 ** (i - 1) * 9
        if dig > n:
            ind = i - 1
            rt = dig - i * 10 ** (i - 1) * 9
            break

    n -= rt
    no = 10 ** ind

    if n == 0:
        print(9)
        return

    u = n
    n -= (n // (ind + 1)) * (ind + 1)
    no += max(0, (u // (ind + 1)) - 1)

    if n == 0:
        print(str(no)[-1])
        return
    else:
        no += 1

    while n > 0:
        if n <= ind + 1:
            e = str(no)
            print(e[n - 1])
        n -= ind + 1
        no += 1


# 示例：根据规模 n 生成测试数据并调用
if __name__ == "__main__":
    # 这里示例生成一个与 n 同值的测试数据，即求第 n 位数字
    # 使用者可按需修改测试数据生成逻辑
    test_n = 1000
    main(test_n)
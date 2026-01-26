def main(n):
    # 根据规模 n 生成测试数据：
    # 构造 list1 为长度 n，由 '+' 和 '-' 构成
    # 构造 list2 为在 list1 的基础上随机替换部分为 '?' 的长度 n 字符串
    # 为了确定性，这里不用随机数，只是简单规则：
    #   前 n//3 个位置与 list1 相同
    #   中间 n//3 个位置用 '?'
    #   剩余位置与 list1 相同
    # 这样可以保证既有 '?' 又有确定符号，且规模由 n 控制。
    list1 = []
    for i in range(n):
        # 交替放 '+' 和 '-'
        list1.append('+' if i % 2 == 0 else '-')
    list2 = []
    for i in range(n):
        if n // 3 <= i < 2 * n // 3:
            list2.append('?')

        else:
            list2.append(list1[i])

    plus1 = list1.count('+')
    plus2 = list2.count('+')
    minus1 = list1.count('-')
    minus2 = list2.count('-')
    wths = list2.count('?')

    def giveFactorial(n, x):
        if x == 0 or x == n or x > n or n == 0:
            return 1

        else:
            return giveFactorial(n - 1, x - 1) + giveFactorial(n - 1, x)

    a = giveFactorial(wths, plus1 - plus2)

    if plus1 == plus2 and wths == 0:
        # print(1)
        pass
    elif wths == 0:
        # print(0)
        pass
    elif plus1 - plus2 > wths or minus1 - minus2 > wths:
        # print(0)
        pass

    else:
        # print((0.5 ** (plus1 - plus2 + minus1 - minus2)) * a)
        pass


# 示例：运行规模为 10
if __name__ == "__main__":
    main(10)
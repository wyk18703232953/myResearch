def main(n: int):
    """
    规模 n 用来生成一组测试数据 [l, r]：
    - 我们让 r = 2^n - 1
    - l = 0
    这样可以测试到同一位数长度且尽可能大的 XOR 情况。
    """
    # 生成测试数据
    l_val = 0
    r_val = (1 << n) - 1  # 2^n - 1

    numeros = [l_val, r_val]

    l = bin(numeros[0])
    r = bin(numeros[1])

    p = -1

    if len(r) == len(l):
        for i in range(len(l)):
            if l[i] != r[i]:
                p = i
                break
        if numeros[0] != numeros[1]:
            saida = 2 ** (len(r) - p) - 1
            print(saida)
        else:
            print(0)
    else:
        if numeros[0] != numeros[1]:
            saida = 2 ** (len(r) - 2) - 1
            print(saida)
        else:
            print(0)


# 示例调用
if __name__ == "__main__":
    # 例如 n = 5，对区间 [0, 31] 求 Little Girl and Maximum XOR
    main(5)
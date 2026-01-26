def main(n):
    # n 作为输入规模，用于生成一对整数 [l, r]
    # 确定性构造：让 r > l，且二者在高位有差异
    # 使用 n 控制数值规模
    if n < 2:
        l_val = 0
        r_val = 0

    else:
        # 保证 r > l，并随 n 增大
        l_val = n
        r_val = 2 * n

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
            # print(saida)
            pass

        else:
            # print(0)
            pass

    else:
        if numeros[0] != numeros[1]:
            saida = 2 ** (len(r) - 2) - 1
            # print(saida)
            pass

        else:
            # print(0)
            pass
if __name__ == "__main__":
    # 示例：使用若干不同规模运行
    for n in [1, 2, 10, 100, 1000]:
        main(n)
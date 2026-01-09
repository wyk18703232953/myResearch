def main(n):
    # 映射规则：
    # 对应原问题两个整数 l, r，规模 n 控制它们的大致数量级
    # l = 2^n，r = 2^(n+1) - 1，可确保 l < r 且有足够位宽
    if n < 1:
        n = 1

    l_val = 1 << n          # 2^n
    r_val = (1 << (n + 1)) - 1  # 2^(n+1) - 1

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
    # 示例调用：可以根据需要修改 n 的大小做规模实验
    main(10)
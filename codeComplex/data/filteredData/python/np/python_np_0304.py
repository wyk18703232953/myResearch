def main(n):
    # 1. 根据规模 n 生成测试数据：
    #    原逻辑需要 n, k，这里让 k 随 n 变化，保证有一定规模且不过大。
    #    可根据需要调整生成规则。
    k = max(1, min(2 * n, n + 5))  # 示例：k 在 [1, 2n] 且约为 n+5

    modulo = 998244353

    # 2. 按原逻辑进行计算：
    if k > 2 * n:
        return 0
    if k == 2 * n or k == 1:
        return 2

    iguales = [0] * (k + 1)
    diferentes = [0] * (k + 1)

    iguales[1] = 2
    diferentes[2] = 2

    for _ in range(1, n):
        auxigual = [0] * (k + 1)
        auxdiff = [0] * (k + 1)
        for j in range(k):
            auxigual[j + 1] = (iguales[j + 1] + iguales[j] + 2 * diferentes[j + 1]) % modulo
            if j >= 1:
                auxdiff[j + 1] = (diferentes[j + 1] + diferentes[j - 1] + 2 * iguales[j]) % modulo

        iguales = auxigual
        diferentes = auxdiff

    return (iguales[-1] + diferentes[-1]) % modulo


# 示例：调用 main(n)，例如：
# print(main(5))
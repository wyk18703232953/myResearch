def main(n):
    # 将原来的 (n, k) 输入结构映射为 (n, k)，其中 k 由 n 确定性生成
    # 这里选择 k = 2*n，用于规模化；当 n 为 0 或 1 时做特殊处理
    if n <= 0:
        return 0
    k = 2 * n

    if k > 2 * n:
        return 0
    if k == 2 * n or k == 1:
        return 2

    iguales = [0] * (k + 1)
    diferentes = [0] * (k + 1)

    iguales[1] = 2
    diferentes[2] = 2

    modulo = 998244353

    for i in range(1, n):
        auxigual = [0] * (k + 1)
        auxdiff = [0] * (k + 1)

        for j in range(1, k + 1):
            auxigual[j] = (iguales[j] + iguales[j - 1] + 2 * diferentes[j]) % modulo

        for kk in range(2, k + 1):
            auxdiff[kk] = (diferentes[kk] + diferentes[kk - 2] + 2 * iguales[kk - 1]) % modulo

        iguales = auxigual
        diferentes = auxdiff

    return (iguales[-1] + diferentes[-1]) % modulo


if __name__ == "__main__":
    # 示例调用，可按需要修改 n 以做规模化实验
    print(main(10))
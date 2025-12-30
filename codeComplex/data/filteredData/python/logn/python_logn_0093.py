import random

def main(n: int):
    """
    n: 规模参数，用来生成测试数据。
       这里用 n 表示 bit 位数（最大数约为 2^n-1）。
    """
    if n <= 0:
        return

    # 生成测试数据：在 [0, 2^n - 1] 范围内随机生成 l, r，并确保 l <= r
    max_val = (1 << n) - 1
    l = random.randint(0, max_val)
    r = random.randint(0, max_val)
    if l > r:
        l, r = r, l

    numeros = [l, r]

    # 原逻辑开始
    l_bin = bin(numeros[0])
    r_bin = bin(numeros[1])

    p = -1

    if len(r_bin) == len(l_bin):
        for i in range(len(l_bin)):
            if l_bin[i] != r_bin[i]:
                p = i
                break
        if numeros[0] != numeros[1]:
            saida = 2 ** (len(r_bin) - p) - 1
            print(saida)
        else:
            print(0)

    else:
        if numeros[0] != numeros[1]:
            saida = 2 ** (len(r_bin) - 2) - 1
            print(saida)
        else:
            print(0)


if __name__ == "__main__":
    # 示例：以 n=10 运行一次
    main(10)
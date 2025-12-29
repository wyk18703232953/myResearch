import random

def solve(l_val, r_val):
    # Original logic wrapped into a function operating on l_val, r_val
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
            return saida
        else:
            return 0
    else:
        if numeros[0] != numeros[1]:
            saida = 2 ** (len(r) - 2) - 1
            return saida
        else:
            return 0


def main(n: int):
    """
    n 为规模参数，用于控制测试数据大小。
    这里简单地将 n 作为最大比特长度来生成随机的 l, r。
    保证 l <= r。
    """
    if n <= 0:
        n = 1

    # 随机生成位数不超过 n 的两个非负整数，且 l <= r
    max_val = (1 << n) - 1  # 最大值为 2^n - 1
    l_val = random.randint(0, max_val)
    r_val = random.randint(l_val, max_val)

    result = solve(l_val, r_val)
    print(result)


if __name__ == "__main__":
    # 示例：使用 n=60 作为规模
    main(60)
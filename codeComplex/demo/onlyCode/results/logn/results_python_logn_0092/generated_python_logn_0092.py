import random

def main(n: int):
    """
    n 用作生成测试数据的规模参数：
    - 生成两个随机整数 l, r
    - 整数的最大值约为 2^n - 1（n 至少为 1）
    """
    if n <= 0:
        n = 1

    # 根据 n 生成测试数据：在 [0, 2^n - 1] 范围内随机取两个数
    max_val = (1 << n) - 1
    l_val = random.randint(0, max_val)
    r_val = random.randint(l_val, max_val)  # 保证 l <= r，符合原题设定

    numeros = [l_val, r_val]

    # 以下为原逻辑（去掉 input() 封装成函数）
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


if __name__ == "__main__":
    # 示例：规模设为 10，可根据需要修改
    main(10)
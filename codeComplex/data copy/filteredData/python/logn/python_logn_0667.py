import math

def main(n):
    # 映射：给定规模 n，构造原程序中的 n, k
    # 例如：保持 n 不变，令 k = n // 2
    original_n = n
    k = n // 2

    variableone = 2 * (original_n + k)
    variabletwo = (-3 + math.sqrt(9 - 4 * 1 * (-1 * variableone))) / 2
    variabletwo = int(variabletwo)
    y = original_n - variabletwo
    # print(y)
    pass
if __name__ == "__main__":
    main(10)
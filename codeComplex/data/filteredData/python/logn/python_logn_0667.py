import math
import random

def main(n):
    # 根据 n 生成测试数据，这里随机生成 k，范围可按需调整
    k = random.randint(0, n)

    variableone = 2 * (n + k)  # the right side of the equation

    # a = 1  b = 3  c = variableone
    # x^2 + 3x - 2(n+k)
    # (-b + squareroot b^2 -4ac) / 2a

    variabletwo = (-3 + math.sqrt(9 - 4 * 1 * (-1 * variableone))) / 2
    variabletwo = int(variabletwo)

    y = n - variabletwo
    print(y)
    return y

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(100)
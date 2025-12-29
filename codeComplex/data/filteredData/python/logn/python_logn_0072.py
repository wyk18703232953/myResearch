import sys
from math import floor
import random


def solve(a: int, b: int) -> int:
    if a == b:
        return 0

    string_1 = ""
    string_2 = ""
    aa = a
    bb = b

    while aa:
        if aa % 2 == 0:
            string_1 = string_1 + "0"
        else:
            string_1 = string_1 + "1"
        aa = floor(aa / 2)

    while bb:
        if bb % 2 == 0:
            string_2 = string_2 + "0"
        else:
            string_2 = string_2 + "1"
        bb = floor(bb / 2)

    lista_1 = list(string_1)
    lista_1.reverse()
    contrario_1 = "".join(lista_1)

    lista_2 = list(string_2)
    lista_2.reverse()
    contrario_2 = "".join(lista_2)

    if len(string_1) != len(string_2):
        resposta = pow(2, len(string_2)) - 1
    else:
        potencia = 0
        for i in range(len(string_1)):
            if contrario_1[i] != contrario_2[i]:
                break
            potencia += 1

        potencia = len(string_1) - potencia
        resposta = pow(2, potencia) - 1

    return resposta


def main(n: int):
    # 根据规模 n 生成测试数据：生成两个 0 <= a, b < 2^n 的随机整数
    if n <= 0:
        a, b = 0, 0
    else:
        max_val = (1 << n) - 1
        a = random.randint(0, max_val)
        b = random.randint(0, max_val)

    # 可以根据需要修改为固定数据，例如：
    # a, b = n, n // 2

    ans = solve(a, b)
    print(ans)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)
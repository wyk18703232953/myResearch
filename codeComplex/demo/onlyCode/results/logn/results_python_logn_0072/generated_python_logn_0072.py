import sys
from math import floor
import random


def main(n: int):
    """
    n 作为规模参数，用来控制生成的测试数据大小。
    这里简单设定：
      - a, b 为 [0, 2^n - 1] 范围内的随机整数（且尽量保证 a != b）
    """
    if n <= 0:
        # 退化情况，给个固定示例
        a, b = 5, 9
    else:
        upper = max(1, 2 ** n - 1)
        a = random.randint(0, upper)
        b = random.randint(0, upper)
        if a == b:  # 尝试让它们不相等
            b = (b + 1) % (upper + 1)

    # ===== 以下为原逻辑改写，无 input() =====

    if a == b:
        print(0)
        return

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

    print(resposta)


if __name__ == "__main__":
    # 示例调用：可根据需要调整 n
    main(5)
# encontrar o máximo xor entre um par que se encontra no intervalo [l,r]

import random

def max_xor_in_range(l: int, r: int) -> int:
    if l == r:
        return 0

    l_bin = bin(l)[2:]
    r_bin = bin(r)[2:]

    if len(l_bin) == len(r_bin):
        i = 1  # ambos começam com 1, não preciso checar
        while i < len(l_bin) and l_bin[i] == r_bin[i]:
            i += 1
        tam = len(l_bin) - i
    else:
        tam = len(r_bin)

    num = ""
    for _ in range(tam):
        num += '1'

    return int(num, 2)


def main(n: int):
    # 根据规模 n 生成测试数据：
    # 取 [0, 2^n - 1] 范围内的随机 l, r，且 l <= r
    if n <= 0:
        # 退化规模，直接输出 0
        print(0)
        return

    upper = (1 << n) - 1
    l = random.randint(0, upper)
    r = random.randint(0, upper)
    if l > r:
        l, r = r, l

    ans = max_xor_in_range(l, r)
    print(ans)
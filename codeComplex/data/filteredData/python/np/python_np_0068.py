from math import factorial
import random

def main(n):
    # 1. 生成测试数据
    # 生成长度为 n 的目标串 s，只包含 '+' 和 '-'
    s = ''.join(random.choice(['+', '-']) for _ in range(n))
    # 生成长度为 n 的带 '?' 的串 s1
    s1 = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    # 2. 原始逻辑
    s = s.rstrip()
    s1 = s1.rstrip()
    pos1 = 0
    pos = 0
    posi = 0
    negi = 0
    posi1 = 0
    negi1 = 0
    ques1 = 0

    for i in s:
        if i == '+':
            pos += 1
            posi += 1
        else:
            pos -= 1
            negi += 1

    for i in s1:
        if i == '+':
            posi1 += 1
        elif i == '-':
            negi1 += 1
        else:
            ques1 += 1

    if posi == posi1 and negi == negi1:
        print(1)
        return

    diff1 = posi - posi1
    diff = negi - negi1

    if diff < 0 or diff1 < 0:
        print(0)
    else:
        outcomes = 2 ** ques1
        nume = factorial(ques1)
        deno = factorial(ques1 - diff1) * factorial(diff1)
        fav1 = nume / deno
        ques1 = ques1 - diff1
        num1 = factorial(ques1)
        deno1 = factorial(ques1 - diff) * factorial(diff)
        fav2 = num1 / deno1
        ans = fav1 * fav2
        print(ans / outcomes)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
from math import factorial
import random

def main(n: int):
    # 1. 随机生成目标串 s1（只含 '+' 和 '-'）
    s1 = ''.join(random.choice(['+', '-']) for _ in range(n))

    # 2. 随机生成观测串 s2（含 '+', '-', '?'）
    #   这里让 '?' 的概率为 1/3，可根据需要调整
    choices = ['+', '-', '?']
    s2 = ''.join(random.choice(choices) for _ in range(n))

    # 以下是原逻辑的封装
    finPos = 0
    for c in s1:
        if c == '+':
            finPos += 1
        else:
            finPos -= 1

    stPos = 0
    for c in s2:
        if c == '+':
            stPos += 1
        elif c == '-':
            stPos -= 1

    qn = s2.count('?')
    diff = abs(finPos - stPos)

    if diff > qn:
        ans = 0.0
    elif (qn & 1) != (diff & 1):
        ans = 0.0
    else:
        i = 0
        for i in range(qn // 2, qn):
            if i * 2 - qn == diff:
                break
        if i * 2 - qn != diff:
            i += 1
        ans = (factorial(qn) / (factorial(qn - i) * factorial(i))) / (1 << qn)

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 10，可自行修改
    main(10)
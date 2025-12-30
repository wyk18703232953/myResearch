from math import factorial, pow
import random

def main(n: int):
    # 生成测试数据：
    # s1: 完全由'+'和'-'组成，长度为 n
    # s2: 由'+', '-', '?'组成，长度为 n
    choices_s1 = ['+', '-']
    choices_s2 = ['+', '-', '?']

    s1 = [random.choice(choices_s1) for _ in range(n)]
    s2 = [random.choice(choices_s2) for _ in range(n)]

    S1 = {"+": 0, "-": 0}
    S2 = {"+": 0, "-": 0, "?": 0}

    for c in s1:
        S1[c] += 1
    for c in s2:
        S2[c] += 1

    if S1["+"] - S2["+"] >= 0 and S1["-"] - S2["-"] >= 0:
        pos = S1["+"] - S2["+"]
        neg = S1["-"] - S2["-"]
        ques = S2["?"]
        if pos + neg == 0 and ques == 0:
            res = 1.0
        else:
            res = (factorial(pos + neg) / (factorial(pos) * factorial(neg))) / pow(2, ques)
        print(f"{res:.12f}")
    else:
        print(f"{0.0:.12f}")


if __name__ == "__main__":
    # 示例：n 可在此修改，或由外部调用 main(n)
    main(10)
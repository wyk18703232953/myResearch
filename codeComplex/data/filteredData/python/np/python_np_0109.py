from math import factorial
import random

def main(n: int):
    # 生成规模为 n 的测试数据 s1, s2
    # s1 只包含 '+' 和 '-'
    # s2 包含 '+', '-', '?' 三种字符
    choices_s1 = ['+', '-']
    choices_s2 = ['+', '-', '?']

    s1 = ''.join(random.choice(choices_s1) for _ in range(n))
    s2 = ''.join(random.choice(choices_s2) for _ in range(n))

    cnt_plus_1, cnt_plus_2 = 0, 0
    cnt_minus_1, cnt_minus_2 = 0, 0
    cnt_question = 0

    for i in range(len(s1)):
        if s1[i] == "+": 
            cnt_plus_1 += 1
        if s1[i] == "-": 
            cnt_minus_1 += 1

        if s2[i] == "+": 
            cnt_plus_2 += 1
        if s2[i] == "-": 
            cnt_minus_2 += 1

        if s2[i] == "?": 
            cnt_question += 1

    if cnt_question == 0:
        if cnt_plus_1 == cnt_plus_2:
            print("{:.9f}".format(1.0))
        else:
            print("{:.9f}".format(0.0))
    elif cnt_plus_2 + cnt_question < cnt_plus_1 or cnt_plus_2 > cnt_plus_1:
        print("{:.9f}".format(0.0))
    else:
        dP = cnt_plus_1 - cnt_plus_2
        dM = cnt_question - dP

        if dM == 0 or dP == 0:
            print("{:0.9f}".format(1 / (2 ** cnt_question)))
        else:
            CP = factorial(cnt_question) / (factorial(dP) * factorial(cnt_question - dP))
            print(CP * (0.5 ** dP) * (0.5 ** (cnt_question - dP)))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
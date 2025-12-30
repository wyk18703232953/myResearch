from math import factorial
import random

def main(n):
    # 生成长度为 n 的 send 字符串，只包含 '+' 和 '-'
    send = ''.join(random.choice('+-') for _ in range(n))

    # 生成长度为 n 的 receive 字符串，包含 '+', '-', '?'
    # 控制比例：大致 1/3 为 '?'
    choices = ['+', '-', '?']
    weights = [1, 1, 1]  # 可以调整比例
    receive = ''.join(random.choices(choices, weights=weights, k=n))

    cntP = send.count("+")
    cntN = send.count("-")

    cnt1 = receive.count("+")
    cnt2 = receive.count("-")

    mark = receive.count("?")

    total = 2 ** mark

    if cntP < cnt1 or cntN < cnt2:
        valid = 0
    else:
        valid = factorial(mark) / factorial(mark - cntP + cnt1) / factorial(cntP - cnt1)

    print(f"{valid / total:0.12f}")

if __name__ == "__main__":
    # 示例：n = 10，可根据需要修改或在外部调用 main(n)
    main(10)
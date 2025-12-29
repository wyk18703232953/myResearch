import math as m
import random

def main(n: int):
    # 1. 生成测试数据
    # 约定：n 为字符串长度，a 和 b 长度相同
    # a: 只包含 '+' 或 '-'，均匀随机
    # b: 包含 '+', '-', '?'，均匀随机
    choices_a = ['+', '-']
    choices_b = ['+', '-', '?']

    a = ''.join(random.choice(choices_a) for _ in range(n))
    b = ''.join(random.choice(choices_b) for _ in range(n))

    # 2. 原逻辑
    total_sum = 0
    req_pos = 0
    unreco = 0

    for i in a:
        if i == '+':
            total_sum += 1
            req_pos += 1
        elif i == '-':
            total_sum -= 1

    for i in b:
        if i == '+':
            total_sum -= 1
            req_pos -= 1
        elif i == '-':
            total_sum += 1
        else:
            unreco += 1

    # 3. 按原程序输出
    if total_sum == 0 and unreco == 0:
        print(1.000000000)
    elif abs(total_sum) > unreco or req_pos < 0:
        print(0.000000000)
    else:
        ans = (m.factorial(unreco) /
               (m.factorial(req_pos) *
                m.factorial(unreco - req_pos) *
                (2 ** unreco)))
        print(ans)


# 示例调用
if __name__ == "__main__":
    main(10)
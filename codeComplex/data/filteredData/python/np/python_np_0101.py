import math
import random

def main(n):
    # 生成测试数据：
    # 构造一个 s1，长度为 n，只包含 '+' 和 '-'，保证正负比较均衡
    s1_list = []
    balance = 0
    for _ in range(n):
        if balance <= 0:
            s1_list.append('+')
            balance += 1
        else:
            s1_list.append('-')
            balance -= 1
    s1 = ''.join(s1_list)

    # 构造一个 s2，长度为 n，只包含 '+', '-', '?'
    # 使得有一定数量的 '?'，便于产生非零概率
    s2_list = []
    for _ in range(n):
        c = random.choice(['+', '-', '?'])
        s2_list.append(c)
    s2 = ''.join(s2_list)

    # 原逻辑
    d1 = 0
    d2 = 0
    num_q = 0
    answer = 0.0

    for ch in s1:
        if ch == '+':
            d1 += 1
        else:
            d1 -= 1

    for ch in s2:
        if ch == '+':
            d2 += 1
        elif ch == '?':
            num_q += 1
        else:
            d2 -= 1

    if num_q >= abs(d2 - d1):
        y = (num_q - abs(d1 - d2)) / 2
        if y % 1 == 0:
            y = int(y)
            # 计算组合数 C(num_q, y) / 2^num_q
            answer = (math.factorial(num_q) /
                      (math.factorial(num_q - y) *
                       math.factorial(y) *
                       (2 ** num_q)))

    print(f"{answer:.9f}")
    return answer

if __name__ == "__main__":
    # 示例: 以 n = 10 运行一次
    main(10)
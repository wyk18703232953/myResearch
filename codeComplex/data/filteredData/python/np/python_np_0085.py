import math
import random

def main(n: int):
    # 生成长度为 n 的目标串 s，只包含 '+' 和 '-'
    s = ''.join(random.choice(['+', '-']) for _ in range(n))

    # 生成长度为 n 的观测串 t，包含 '+', '-', '?'（模拟未知）
    # 这里设置每个字符的概率，可根据需要调整
    choices = ['+', '-', '?']
    probs = [0.4, 0.4, 0.2]  # 对应 '+', '-', '?'
    t = ''.join(random.choices(choices, probs, k=n))

    p1 = m1 = p2 = m2 = q = 0

    for ch in s:
        if ch == '+':
            p1 += 1
        else:
            m1 += 1

    for ch in t:
        if ch == '+':
            p2 += 1
        elif ch == '-':
            m2 += 1
        else:
            q += 1

    dp, dm = p1 - p2, m1 - m2
    if dp < 0 or dm < 0:
        ans = 0.0
    else:
        ans = (math.factorial(q) /
               (math.factorial(dp) * math.factorial(dm))) / math.pow(2, q)

    print(ans)

if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)
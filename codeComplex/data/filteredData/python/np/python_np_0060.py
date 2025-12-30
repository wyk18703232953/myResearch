from math import factorial as f
import random

def main(n: int):
    # 1. 生成测试数据（规模由 n 控制）
    # 随机生成目标串 target 和当前串 s，长度均为 n
    # 字符只在 '+' 和 '-' 中随机选择，s 中再随机若干位置改为 '?'
    target = ''.join(random.choice(['+', '-']) for _ in range(n))
    s_list = []
    for _ in range(n):
        c = random.choice(['+', '-', '?'])
        s_list.append(c)
    s = ''.join(s_list)

    # 2. 原逻辑计算
    quest = s.count("?")
    plusn = target.count("+")
    plus = s.count("+")

    try:
        need_plus_from_q = plusn - plus
        if need_plus_from_q < 0 or need_plus_from_q > quest:
            raise ValueError("impossible")
        comb = f(quest) / (f(need_plus_from_q) * f(quest - need_plus_from_q))
        ans = comb / (2 ** quest)
    except Exception:
        ans = 0.0

    print(f"{ans:.12f}")

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)
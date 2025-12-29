import math
import random

def main(n):
    # 生成规模为 n 的测试数据：字符串 s, t
    # s 和 t 的长度都设为 n
    # s 只包含 '+' 和 '-'，随机生成
    # t 在 '+', '-', '?' 中随机生成
    s = ''.join(random.choice(['+', '-']) for _ in range(n))
    t = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    # 原逻辑开始
    p = 0
    for c in s:
        if c == '+':
            p += 1

    pt, qt = 0, 0
    for c in t:
        if c == '+':
            pt += 1
        elif c == '?':
            qt += 1

    req = p - pt
    if req > qt or req < 0:
        ans = 0.0
    else:
        # 计算组合数 C(qt, req) / 2^qt
        ans = math.factorial(qt) / math.factorial(req)
        ans /= math.factorial(qt - req)
        ans /= pow(2, qt)

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
import math
import random

def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)

def main(n):
    """
    n 为规模参数，用于生成测试数据长度。
    我们生成两个长度为 n 的字符串 s1, s2：
    s1 只含 '+' 和 '-'；
    s2 含 '+', '-', '?'。
    然后对这两个字符串执行原程序的逻辑。
    """
    # 生成测试数据
    # s1: 仅由 '+' 和 '-' 组成
    s1 = ''.join(random.choice(['+', '-']) for _ in range(n))
    # s2: 由 '+', '-', '?' 组成
    s2 = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    dict1 = {'+': 0, '-': 0, '?': 0}

    # 第一行：统计 s1 中 '+' 和 '-' 的数量
    for ch in s1:
        dict1[ch] += 1

    # 第二行：根据 s2 更新计数
    for ch in s2:
        if ch == '?':
            dict1[ch] += 1
        else:
            dict1[ch] -= 1

    # 原逻辑
    if dict1['+'] < 0 or dict1['-'] < 0:
        print("0.000000000000")
    elif dict1['+'] == 0 and dict1['-'] == 0:
        print("1.000000000000")
    elif dict1['+'] and dict1['-']:
        ans = nCr(dict1['?'], dict1['+']) / (2 ** dict1['?'])
        print(f"{ans:.12f}")
    else:
        ans = 1 / (2 ** dict1['?'])
        print(f"{ans:.12f}")

# 示例调用
if __name__ == "__main__":
    main(10)
import random
import string

def main(n):
    # 生成规模为 n 的测试数据：
    # 原代码中有 n, m 和两个字符串 a, b。
    # 这里我们令：
    #   - a 的长度为 n
    #   - b 的长度为 m（m 在 [max(1, n-2), n+2] 范围内随机）
    #   - 保证 a 中至少有一个 '*'，但有一定概率没有（模拟原逻辑的两种分支）

    # 生成模式串 a
    # 50% 概率生成含 '*' 的模式，50% 概率为完全普通字符串
    has_star = random.choice([True, False])
    alphabet = string.ascii_lowercase

    if has_star and n >= 1:
        # 随机选择 '*' 出现的位置（至少一个）
        # 简化：只生成一个 '*'
        star_pos = random.randint(0, n - 1)
        a_chars = []
        for i in range(n):
            if i == star_pos:
                a_chars.append('*')
            else:
                a_chars.append(random.choice(alphabet))
        a = ''.join(a_chars)
    else:
        # 不含 '*'
        if n == 0:
            a = ''
        else:
            a = ''.join(random.choice(alphabet) for _ in range(n))

    # 生成 b 的长度 m（允许和 a 有差别）
    m = random.randint(max(1, max(0, n - 2)), n + 2)
    b = ''.join(random.choice(alphabet) for _ in range(m))

    # 以下为原逻辑的实现
    flag = 0
    for c in a:
        if c == '*':
            flag = 1

    if flag == 1:
        a1, a2 = a.split('*')
        Len1 = len(a1)
        Len2 = len(a2)
        b1 = b[:Len1]
        b2 = ''
        if Len2:
            b2 = b[-Len2:]
        if a1 == b1 and a2 == b2 and Len1 + Len2 <= len(b):
            print('YES')
        else:
            print('NO')
    else:
        if a == b:
            print('YES')
        else:
            print('NO')

    # 如需调试，可返回生成的数据：
    # return a, b, n, m

if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次测试
    main(10)
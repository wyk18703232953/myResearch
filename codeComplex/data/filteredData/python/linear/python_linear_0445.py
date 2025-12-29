import random
import string


def main(n: int):
    """
    n 作为规模参数，用来控制生成字符串的最大长度。
    逻辑：
    - 生成一个模式串 a，长度在 [1, n]，包含至多一个 '*'（随机决定是否含有 '*'）。
    - 生成一个待匹配串 b，长度在 [1, n]。
    - 按照原程序逻辑判断并打印 YES/NO。
    """

    if n <= 0:
        return

    # 随机生成模式串 a（可能含有 0 或 1 个 '*'）
    # 先随机决定是否包含 '*'
    has_star = random.choice([True, False])

    # 字符集：小写字母
    chars = string.ascii_lowercase

    if has_star:
        # 保证长度至少为 1，最多 n
        length_a = random.randint(1, n)
        # 至少要有一个位置留给 '*'
        if length_a == 1:
            # 只能是 '*' 本身
            a = '*'
        else:
            # 在 [0, length_a - 1] 位置中选一个位置放 '*'
            star_pos = random.randint(0, length_a - 1)
            a_list = []
            for i in range(length_a):
                if i == star_pos:
                    a_list.append('*')
                else:
                    a_list.append(random.choice(chars))
            a = ''.join(a_list)
    else:
        # 不含 '*'，长度 [1, n]
        length_a = random.randint(1, n)
        a = ''.join(random.choice(chars) for _ in range(length_a))

    # 生成待匹配串 b，长度 [1, n]
    length_b = random.randint(1, n)
    b = ''.join(random.choice(chars) for _ in range(length_b))

    # ---------------- 原始逻辑开始 ----------------
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
    # ---------------- 原始逻辑结束 ----------------


if __name__ == "__main__":
    # 示例：使用 n = 10 运行一次
    main(10)
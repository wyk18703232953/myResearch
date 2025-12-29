import random
import string


def main(n):
    """
    n 为规模参数，用来生成测试数据：
    - m 在 [max(1, n-3), n+3] 范围内随机生成
    - s 为长度为 n 的模式串，含 0 或 1 个 '*'
    - t 为长度为 m 的普通字符串（无 '*'）
    """

    # 生成 m（长度与 n 接近）
    m = random.randint(max(1, n - 3), n + 3)

    # 决定是否在 s 中放置 '*'
    has_star = random.choice([True, False])
    alphabet = string.ascii_lowercase

    if not has_star:
        # 不含 '*'
        s = ''.join(random.choice(alphabet) for _ in range(n))
    else:
        # 含一个 '*'
        if n == 1:
            s = '*'
        else:
            star_pos = random.randint(0, n - 1)
            chars = []
            for i in range(n):
                if i == star_pos:
                    chars.append('*')
                else:
                    chars.append(random.choice(alphabet))
            s = ''.join(chars)

    # 生成 t：长度为 m，普通字符串
    t = ''.join(random.choice(alphabet) for _ in range(m))

    # ===== 原逻辑开始 =====
    if '*' not in s:
        if s == t:
            print('YES')
        else:
            print('NO')
    elif n > m + 1:
        print('NO')
    elif n == 1 and s == '*':
        print('YES')
    else:
        s_list = list(s)
        t_list = list(t)
        if s_list[0] == '*':
            if s_list[1:] == t_list[-len(s_list[1:]):]:
                print('YES')
            else:
                print('NO')
        elif s_list[-1] == '*':
            if s_list[:n - 1] == t_list[:n - 1]:
                print('YES')
            else:
                print('NO')
        else:
            ind = s_list.index('*')
            if (
                s_list[:ind] == t_list[:ind]
                and s_list[ind + 1:] == t_list[-len(s_list[ind + 1:]):]
            ):
                print('YES')
            else:
                print('NO')
    # ===== 原逻辑结束 =====

    # 如需调试，可打印生成的测试数据：
    # print("n =", n, "m =", m)
    # print("s =", s)
    # print("t =", t)


if __name__ == "__main__":
    # 示例运行：规模为 5
    main(5)
import random
import string


def solve(n, m, s, t):
    s = list(s)
    t = list(t)
    idx = -1
    for i in range(n):
        if s[i] == '*':
            idx = i
    if idx == -1:
        if s == t:
            print('YES')
        else:
            print('NO')
    else:
        if m < n - 1:
            print('NO')
        else:
            s_left = s[0:idx]
            s_right = s[idx + 1:n]
            a = len(s_left)
            b = len(s_right)
            t_left = []
            t_right = []
            for i in range(a):
                t_left.append(t[i])
                t[i] = ''
            for i in range(b):
                t_right.append(t[m - i - 1])
            if s_left == t_left and s_right == t_right[::-1]:
                print('YES')
            else:
                print('NO')


def generate_test_data(n):
    """
    生成规模为 n 的测试数据 (n, m, s, t)
    约定：
      - 字符集使用小写字母
      - 当生成的 s 包含 '*' 时，t 的长度 m 随机选择 [n-1, n+2] 之间
      - 当 s 不含 '*' 时，t 的长度 m = n
    """
    alphabet = string.ascii_lowercase

    # 随机决定是否包含 *
    has_star = random.choice([True, False])

    if not has_star:
        # 生成长度为 n 的串 s、t（无 *）
        s = ''.join(random.choice(alphabet) for _ in range(n))
        # t 有时等于 s，有时随机
        if random.choice([True, False]):
            t = s
        else:
            t = ''.join(random.choice(alphabet) for _ in range(n))
        m = n
        return n, m, s, t
    else:
        # 至少长度 1（若 n == 1，则只能是 "*"）
        if n == 1:
            s = '*'
            # m 随机在 [0, 3] 中取一个 >= 0 的整数
            m = random.randint(0, 3)
            t = ''.join(random.choice(alphabet) for _ in range(m))
            return n, m, s, t

        # 随机选择 * 的位置
        star_pos = random.randint(0, n - 1)
        s_list = []
        for i in range(n):
            if i == star_pos:
                s_list.append('*')
            else:
                s_list.append(random.choice(alphabet))
        s = ''.join(s_list)

        # t 的长度在 [max(0, n-1), n+2] 范围内
        low = max(0, n - 1)
        high = n + 2
        m = random.randint(low, high)
        t = ''.join(random.choice(alphabet) for _ in range(m))
        return n, m, s, t


def main(n):
    # 根据规模 n 生成测试数据
    n_val, m_val, s, t = generate_test_data(n)
    # 打印生成的数据，便于观察（可根据需要注释）
    print(f"n = {n_val}, m = {m_val}")
    print(f"s = {s}")
    print(f"t = {t}")
    # 调用原逻辑
    solve(n_val, m_val, s, t)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改或在外部调用 main(n)
    main(10)
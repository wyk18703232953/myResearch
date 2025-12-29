import random
import string

def main(n):
    # 1. 生成测试数据规模
    # n 为字符串 s 的长度
    # 生成 m，保证 1 <= m <= 2n，且满足原程序中可能的各种分支
    m = random.randint(1, 2 * n)

    # 2. 随机生成 s 和 t（包含和不包含 '*' 的情况）
    #   - s 长度为 n
    #   - t 长度为 m
    # 随机决定 s 是否含有 '*'
    has_star = random.choice([True, False])

    # 可用字符集合（不含 '*'）
    letters = string.ascii_lowercase

    if has_star and n > 0:
        # 在某个位置放一个 '*'
        star_pos = random.randint(0, n - 1)
        s_chars = []
        for i in range(n):
            if i == star_pos:
                s_chars.append('*')
            else:
                s_chars.append(random.choice(letters))
        s = ''.join(s_chars)
    else:
        # 不含 '*'
        s = ''.join(random.choice(letters) for _ in range(n))

    # 生成 t：完全随机
    t = ''.join(random.choice(letters) for _ in range(m))

    # 3. 以下是原逻辑（去掉 input，封装函数内，使用生成的 n, m, s, t）
    # 输出 n, m, s, t 用于观察测试数据
    print(f"n = {n}, m = {m}")
    print(f"s = {s}")
    print(f"t = {t}")

    if n - 1 > m:
        print('NO')
    else:
        try:
            a = s.index('*')
        except ValueError:
            a = -1

        if a == -1:
            if s == t:
                print('YES')
            else:
                print('NO')
        else:
            for i in range(a):
                if s[i] != t[i]:
                    print('NO')
                    return
            i = 1
            while m - i >= a and n - i > a:
                if s[n - i] != t[m - i]:
                    print('NO')
                    return
                i += 1
            print('YES')


# 示例调用
if __name__ == "__main__":
    # 可以修改 n 以生成不同规模的测试
    main(10)
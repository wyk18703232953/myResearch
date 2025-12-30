import random
import string

def main(n):
    # 生成规模为 n 的模式串 a（长度为 n），以及文本串 b（长度为 m）
    # 规则：随机决定是否包含 '*'，以及 b 的长度 m（在 [max(1, n-1), n+3] 之间）
    if n <= 0:
        return

    # 随机决定是否在模式串中放置一个 '*'
    has_star = random.choice([True, False])

    if has_star and n >= 2:
        # 在 [0, n-1] 之间选一个位置放 '*'
        star_pos = random.randint(0, n - 1)
        # 其他位置填充随机小写字母
        chars = []
        for i in range(n):
            if i == star_pos:
                chars.append('*')
            else:
                chars.append(random.choice(string.ascii_lowercase))
        a = ''.join(chars)
    else:
        # 不含 '*'
        a = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 确定 b 的长度 m：允许稍短、相等、稍长
    m = random.randint(max(1, n - 1), n + 3)
    b = ''.join(random.choice(string.ascii_lowercase) for _ in range(m))

    # 将原逻辑直接改写为函数体：用生成的 a, b, n, m
    if '*' in a:
        c = a.replace('*', '')
        i = a.index('*')
        if c == b:
            print("YES")
        elif a[:i] == b[:i]:
            t = a[i + 1:]
            tt = b[m - n + 1 + i:]
            if t == tt and n - 1 <= m:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    elif n > m:
        print("NO")
    else:
        if a == b:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可在外层自行多次调用
    main(5)
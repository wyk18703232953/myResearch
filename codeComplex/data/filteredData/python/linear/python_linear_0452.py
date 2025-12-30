import random
import string

def generate_test_data(n):
    # 随机生成 m，保证 m >= 1
    # 为了覆盖更多情况，让 m 在 [max(1, n-2), n+2] 范围内浮动
    m = random.randint(max(1, n - 2), n + 2)

    # 随机生成模式串 s，长度为 n，包含小写字母和'*'
    chars = string.ascii_lowercase + '*'
    s = ''.join(random.choice(chars) for _ in range(n))

    # 随机生成目标串 t，长度为 m，仅小写字母
    t = ''.join(random.choice(string.ascii_lowercase) for _ in range(m))

    return n, m, s, t

def solve(n, m, s, t):
    if n == 1:
        if s == t or s == '*':
            return 'YES'
        else:
            return 'NO'
    elif s.count('*') == 0:
        if s == t:
            return 'YES'
        else:
            return 'NO'
    elif n > m + 1:
        return 'NO'
    else:
        l = s.split('*')
        x = t[:len(l[0])]
        y = t[-len(l[1]):] if len(l[1]) > 0 else ''
        if (l[0] == x and l[1] == y) or (s[:1] == '*' and l[1] == y) or (l[0] == x and s[-1:] == '*'):
            return 'YES'
        else:
            return 'NO'

def main(n):
    n, m, s, t = generate_test_data(n)
    ans = solve(n, m, s, t)
    print(ans)

# 示例调用：
# main(5)
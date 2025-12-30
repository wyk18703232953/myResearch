import random
import string


def main(n):
    # 随机生成 1 <= k <= n
    k = random.randint(1, n)

    # 随机生成长度为 n 的小写字母串 s
    letters = string.ascii_lowercase
    s = ''.join(random.choice(letters) for _ in range(n))

    # 原程序逻辑开始
    m = -1
    for i in range(0, n - 1):
        ff = 0
        for j in range(0, i + 1):
            if s[j] != s[n - i - 1 + j]:
                ff = 1
                break
        if ff == 0:
            m = i

    print(s, end="")
    for _ in range(1, k):
        for j in range(m + 1, n):
            print(s[j], end="")
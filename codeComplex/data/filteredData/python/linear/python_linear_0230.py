import random
import string

def main(n: int):
    # 生成一个长度为 n 的随机字符串，字符从 'a' 到 'z' 中选取
    # 为了保持与原程序相似的行为，确保包含一定概率的 'x'
    letters = string.ascii_lowercase
    s = ''.join(random.choice(letters) for _ in range(n))

    # 原逻辑开始
    size = n

    ct = 0
    F = 0
    for i in range(size - 2):
        if s[i] == s[i + 1] and s[i + 1] == s[i + 2] and s[i] == 'x':
            ct += 1
            F = 1

    if F == 0:
        print(0)
    else:
        print(ct)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)
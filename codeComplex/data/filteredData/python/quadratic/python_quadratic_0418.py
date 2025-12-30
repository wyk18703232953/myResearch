import random
import string

def main(n, k=None):
    # 若未提供 k，则随机生成一个合理的 k（至少 1）
    if k is None:
        k = random.randint(1, max(1, n))

    # 随机生成长度为 n 的小写字母串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    i = -1
    for j in range(n - 1):
        if s[:j + 1] == s[n - j - 1:]:
            i = j
    add = s[i + 1:]
    for _ in range(k - 1):
        s += add
    print(s)


if __name__ == "__main__":
    # 示例调用：规模 n=5，可根据需要修改或在外部调用 main(n, k)
    main(5)
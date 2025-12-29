import random
import string

def main(n: int):
    # 生成规模为 n 的测试数据：n 个麻将牌字符串，每个为 "<字母><数字>"
    # 字母从 'a' 到 'z'，数字从 '1' 到 '9'
    s = []
    for _ in range(n):
        rank = random.choice(string.ascii_lowercase[:9])  # a-i
        suit = random.choice('123')
        s.append(rank + suit)

    # 为了与原逻辑一致，仅取前三个元素进行判断
    s = s[:3]
    s.sort()

    # 原始逻辑开始
    if s[0] == s[1] == s[2]:
        print(0)
        return

    if s[0][1] == s[1][1] == s[2][1]:
        if ord(s[0][0]) + 1 == ord(s[1][0]) == ord(s[2][0]) - 1:
            print(0)
            return

    if (s[0][1] == s[1][1] and ord(s[0][0]) + 2 >= ord(s[1][0]) or
        s[1][1] == s[2][1] and ord(s[1][0]) + 2 >= ord(s[2][0]) or
        s[0][1] == s[2][1] and ord(s[0][0]) + 2 >= ord(s[2][0])):
        print(1)
        return

    if s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
        print(1)
        return

    print(2)


if __name__ == "__main__":
    # 示例：规模 n = 3
    main(3)
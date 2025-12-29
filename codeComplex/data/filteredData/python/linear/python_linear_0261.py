import random
import string

def main(n):
    # 生成长度为 n 的随机字符串，字符来自小写字母
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    c = c1 = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - i - 1]:
            c += 1
    for i in range(len(s)):
        if s[i] == s[0]:
            c1 += 1

    if c1 == len(s):
        print(0)
    elif c == len(s) // 2:
        print(len(s) - 1)
    else:
        print(len(s))


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此处调整
    main(10)
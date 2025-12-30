import random
import string

def podstroka(s: str):
    m = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if sub in m:
                m[sub] += 1
            else:
                m[sub] = 1
    return m

def main(n: int):
    # 根据规模 n 生成一个随机字符串，使用小写字母
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    m = podstroka(s)

    maxlen = 0
    for x in m:
        if m[x] >= 2 and len(x) > maxlen:
            maxlen = len(x)

    print(maxlen)

# 示例：运行 main(10)
if __name__ == "__main__":
    main(10)
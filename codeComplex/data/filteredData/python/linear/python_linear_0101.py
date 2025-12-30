import random
import string

def main(n: int):
    # 生成两个长度约为 n 的随机字符串，字符集为小写字母
    len1 = max(1, n)
    len2 = max(1, n)
    s1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(len1))
    s2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(len2))

    output = s1 + s2
    for j in range(len(s1)):
        s = s1[:j + 1]
        for k in range(len(s2)):
            s += s2[k]
            if sorted([s, output])[0] == s:
                output = s
    print(output)


if __name__ == "__main__":
    # 示例：n = 5
    main(5)
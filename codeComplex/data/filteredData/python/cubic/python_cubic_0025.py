import random
import string

def main(n: int):
    # 生成长度为 n 的测试字符串，由小写字母构成
    # 为了更容易产生重复子串，限制字符集为前 min(5, 26) 个字母
    alphabet_size = min(5, 26)
    chars = string.ascii_lowercase[:alphabet_size]
    s = ''.join(random.choice(chars) for _ in range(n))

    leng = 0
    # 原逻辑：在字符串 s 中寻找最长的重复子串长度
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if s.count(sub) >= 2 and len(sub) > leng:
                leng = len(sub)
            elif s.count(sub) == 1:
                for k in range(1, len(sub)):
                    if i - k >= 0 and s[i - k:j - k] == sub and len(sub) > leng:
                        leng = len(sub)
    print(leng)

if __name__ == "__main__":
    # 示例：规模 n = 100
    main(100)
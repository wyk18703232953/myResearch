import random
import string as strlib

def main(n: int):
    # 生成长度为 n 的随机小写字母串
    s = ''.join(random.choice(strlib.ascii_lowercase) for _ in range(n))

    mx = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            m = 0
            while j + m < len(s) and s[i + m] == s[j + m]:
                m += 1
            mx = max(mx, m)

    print(mx)

if __name__ == "__main__":
    # 示例：n 可根据需要调整
    main(10)
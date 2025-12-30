import random
import string

def main(n: int):
    # 1. 生成长度为 n 的随机字符串，字符集为小写字母
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    res = 0
    solve = 0
    # 2. 保持原始逻辑
    for pos in range(1, len(s)):
        for i in range(len(s) - pos):
            if s[i:i + pos] in s[i + 1:]:
                if solve < pos:
                    solve = pos
    print(solve)

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)
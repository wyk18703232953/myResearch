import random
import string

def main(n: int) -> int:
    # 1. 生成长度为 n 的随机字符串，字符集为小写字母
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    res = 0
    # 2. 原始逻辑：寻找最长重复子串（可重叠）
    for i in range(len(s)):
        for j in range(i, len(s)):
            for f in range(i + 1, len(s)):
                if len(s) >= f + (j - i):
                    if s[i:j] == s[f:f + (j - i)]:
                        res = max(res, j - i)

    # 3. 返回结果而不是打印
    return res

if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要调整 n
    print(main(10))
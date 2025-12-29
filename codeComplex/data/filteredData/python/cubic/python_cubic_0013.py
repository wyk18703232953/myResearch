import random
import string

def main(n: int):
    # 1. 生成长度为 n 的随机字符串，字符集为小写字母
    if n <= 0:
        print(0)
        return
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 原逻辑：求最长重复子串的长度（可重叠）
    n = len(s)
    m = n - 1
    while m > 0:
        f = False
        for i in range(0, n - m):
            for j in range(i + 1, n - m + 1):
                x = True
                for k in range(0, m):
                    if s[i + k] != s[j + k]:
                        x = False
                        break
                if x:
                    f = True
                    break
            if f:
                break
        if f:
            break
        m -= 1
    print(m)

if __name__ == "__main__":
    # 示例：规模为 10，可按需修改
    main(10)
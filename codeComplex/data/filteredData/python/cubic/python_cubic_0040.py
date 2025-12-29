import random
import string

def main(n: int):
    # 生成长度为 n 的随机字符串，字符集为小写字母
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    n_len = len(s)
    m = n_len - 1
    while m > 0:
        find = False
        for i in range(0, n_len - m):
            for j in range(i + 1, n_len - m + 1):
                match = True
                for k in range(0, m):
                    if s[i + k] != s[j + k]:
                        match = False
                        break
                if match:
                    find = True
                    break
            if find:
                break
        if find:
            break
        m -= 1
    print(m)

# 示例调用
if __name__ == "__main__":
    main(10)
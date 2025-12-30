import random
import string

def is_pal(s):
    return s == s[::-1]

def main(n):
    # 生成长度为 n 的随机小写字母串作为测试数据
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    if not is_pal(s):
        print(len(s))
    else:
        not_eq = False
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                print(len(s) - 1)
                not_eq = True
                break
        if not not_eq:
            print(0)

# 示例调用
if __name__ == "__main__":
    main(10)
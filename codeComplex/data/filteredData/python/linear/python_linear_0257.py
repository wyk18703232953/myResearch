import random
import string

def palin(s):
    if s[::-1] != s or len(s) == 0:
        return len(s)
    else:
        return palin(s[1:])

def main(n):
    # 根据规模 n 生成长度为 n 的随机字符串
    # 字符集可根据需要调整
    chars = string.ascii_lowercase
    s = ''.join(random.choice(chars) for _ in range(n))
    # 输出结果
    print(palin(s))

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
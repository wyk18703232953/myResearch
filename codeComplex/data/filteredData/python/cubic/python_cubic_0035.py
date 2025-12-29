import random
import string

def main(n: int):
    # 生成长度为 n 的测试字符串，字符集为小写字母
    s = ''.join(random.choices(string.ascii_lowercase, k=n))

    m = 0
    length = len(s)
    for i in range(length):
        for j in range(i, length + 1):
            if s[i:j] in s[i + 1:length] and len(s[i:j]) > m:
                m = len(s[i:j])
    print(m)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
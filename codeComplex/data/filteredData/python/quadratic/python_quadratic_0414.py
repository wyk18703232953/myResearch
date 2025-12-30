import random
import string

def main(n: int):
    # 生成测试数据：
    # 1) 随机选择 k 的范围，这里设为 1~n
    # 2) 生成长度为 n 的随机小写字符串 s
    if n <= 0:
        return

    k = random.randint(1, max(1, n))
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 原逻辑
    for i in range(1, n):
        if s[:n - i] == s[i:]:
            print(s + s[n - i:] * (k - 1))
            return
    print(s * k)


if __name__ == "__main__":
    # 示例：可在此处手动调用 main 进行本地测试
    main(5)
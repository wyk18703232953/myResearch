import random
import string

def main(n: int):
    # 生成测试数据：长度为 n 的两个随机字符串 a、b（字母表可按需修改）
    alphabet = string.ascii_lowercase
    a = ''.join(random.choice(alphabet) for _ in range(n))
    b = ''.join(random.choice(alphabet) for _ in range(n))

    # 原始逻辑
    c = [10**10 for _ in range(n + 10)]
    c[0] = 0 if a[0] == b[0] else 1

    for i in range(1, n):
        if a[i] == b[i]:
            c[i] = c[i - 1]
        elif a[i] == b[i - 1] and a[i - 1] == b[i]:
            c[i] = (1 + c[i - 2] if i > 1 else 1)
        c[i] = min(c[i], c[i - 1] + 1)

    print(c[n - 1])

if __name__ == "__main__":
    # 示例：n = 10
    main(10)
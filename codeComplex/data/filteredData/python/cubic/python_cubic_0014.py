import random
import string

def main(n: int):
    # 3. 根据 n 生成测试数据：随机生成一个长度为 n 的小写字母串
    a = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 原逻辑
    n = len(a)
    for i in range(n - 1, -1, -1):
        b = sorted(a[j:j + i] for j in range(n - i + 1))
        if True in [b[j] == b[j - 1] for j in range(1, n - i + 1)]:
            print(i)
            break

# 示例调用
if __name__ == "__main__":
    main(10)
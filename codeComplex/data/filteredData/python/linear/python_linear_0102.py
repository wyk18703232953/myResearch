import random
import string

def main(n: int):
    # 1. 根据规模 n 生成测试数据
    # 设定 a 的长度为 n，b 的长度为 1（原逻辑只用到 b[0]）
    a_length = max(1, n)  # 保证至少长度为 1
    a = ''.join(random.choices(string.ascii_lowercase, k=a_length))
    b = random.choice(string.ascii_lowercase)

    # 2. 原始逻辑
    li = []
    for i in range(len(a)):
        li.append(a[:i + 1] + b[0])
    li.sort()
    print(li[0])

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
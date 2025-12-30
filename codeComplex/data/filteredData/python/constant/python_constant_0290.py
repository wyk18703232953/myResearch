import random

def main(n: int):
    # 根据规模 n 生成测试数据：从 0 到 n 的随机整数
    x = random.randint(0, n)

    d = x // 2
    print(d + 1)

if __name__ == "__main__":
    # 示例：可在此处指定规模 n
    main(100)
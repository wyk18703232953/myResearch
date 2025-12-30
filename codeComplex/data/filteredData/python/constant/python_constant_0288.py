import random

def main(n: int):
    # 生成测试数据：随机生成一个 0 到 n 之间的整数
    x = random.randint(0, n)
    # 原逻辑：print(int(input()) // 2 + 1)
    result = x // 2 + 1
    print(result)

if __name__ == "__main__":
    # 示例：用规模 n = 100 运行
    main(100)
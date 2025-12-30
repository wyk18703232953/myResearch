import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里简单设为 n 本身
    a = n
    # 如果你希望是随机测试数据，可以改为：
    # a = random.randint(0, n)
    print((a // 2) * 3)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
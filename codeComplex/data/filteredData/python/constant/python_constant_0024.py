import random

def main(n):
    # 根据规模 n 生成测试数据，这里简单设为 n
    a = n
    # 或者使用随机生成：a = random.randint(0, n)

    result = (a // 2) * 3
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
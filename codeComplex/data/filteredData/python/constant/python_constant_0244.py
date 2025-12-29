import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 设 m 为一个 0 到 2^(n+1)-1 之间的随机整数
    upper_bound = 2 ** (n + 1)
    m = random.randint(0, upper_bound - 1)

    # 原逻辑：输出 m % (2**n)
    result = m % (2 ** n)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
import random

def main(n):
    # 根据 n 生成测试数据：
    # 这里简单设定 k 为 1 到 n^2 之间的随机整数
    k = random.randint(1, n * n)

    # 原逻辑：输出 ceil(k / n)
    result = (k + n - 1) // n
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
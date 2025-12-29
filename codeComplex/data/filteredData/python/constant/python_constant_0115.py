import random

def main(n):
    # 根据规模 n 生成测试数据：在 [-10^n + 1, 10^n - 1] 范围内随机生成一个整数
    if n <= 0:
        value = 0
    else:
        limit = 10 ** n - 1
        value = random.randint(-limit, limit)

    # 以下为原始逻辑，作用于随机生成的 value
    if value > -1:
        result = value
    else:
        s = str(value)
        x = int(s[:len(s) - 1])
        y = int(s[:len(s) - 2] + s[-1])
        result = max(x, y)

    print(result)

if __name__ == "__main__":
    # 示例：以规模 n=3 运行
    main(3)
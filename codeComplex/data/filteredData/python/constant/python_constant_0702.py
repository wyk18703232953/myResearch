import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 题意：原本是从输入读取 n 和 v，这里我们用参数 n 和随机生成的 v
    # 保证 1 <= v <= n
    if n <= 0:
        return  # 或者根据需要处理非法 n

    v = random.randint(1, n)

    # 原逻辑
    if n < v + 2:
        result = n - 1
    else:
        result = int(v - 1 + (n - v) * (n - v + 1) / 2)

    print(result)


if __name__ == '__main__':
    # 示例：调用 main，n 作为规模参数
    main(10)
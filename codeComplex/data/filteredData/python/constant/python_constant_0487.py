import random

def main(n):
    # 根据 n 生成测试数据
    # 这里假设 k 的规模与 n 同级，可根据需要调整
    k = random.randint(1, max(1, 10 * n))

    # 原逻辑：输出 -(-k // n)
    result = -(-k // n)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，指定规模 n
    main(10)
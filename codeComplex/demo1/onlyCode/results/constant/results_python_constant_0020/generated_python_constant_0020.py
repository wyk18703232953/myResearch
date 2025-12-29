import random

def f(n):
    return n + n // 2

def main(n):
    # 生成测试数据，这里假设需要一个整数作为测试
    # 根据规模 n，我们生成一个 1 到 n 范围内的随机整数
    test_value = random.randint(1, max(1, n))
    result = f(test_value)
    print(result)

if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)
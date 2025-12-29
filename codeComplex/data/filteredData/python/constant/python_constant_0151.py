import random

def main(n):
    # 生成一个整数作为测试数据，这里在 [0, n] 范围内
    i = random.randint(0, n)

    d = i % 2 + 8
    print(d, i - d)

if __name__ == "__main__":
    # 示例：将规模设为 100
    main(100)
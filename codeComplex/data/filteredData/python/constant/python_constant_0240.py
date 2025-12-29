import random

def main(n: int):
    # 根据规模 n 生成测试数据 m
    # 这里简单设定 m 为一个与规模相关的随机整数
    random.seed(0)
    m = random.randint(0, 10**6 * max(1, n))

    # 原始逻辑
    if n <= 26:
        print(m % (2 ** n))
    else:
        print(m)

# 示例调用（实际使用时可由外部调用 main(n)）
if __name__ == "__main__":
    main(10)
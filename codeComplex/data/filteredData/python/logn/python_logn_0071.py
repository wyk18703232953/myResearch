import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里构造两个 0 ~ 2^n-1 之间的整数
    # 可根据需要调整数据生成策略
    upper = (1 << n) - 1
    l = random.randint(0, upper)
    r = random.randint(0, upper)

    # 原始逻辑
    p = l ^ r
    x = 1
    while x <= p:
        x = x << 1
    print(x - 1)

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)
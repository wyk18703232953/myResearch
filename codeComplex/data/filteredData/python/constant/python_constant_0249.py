import random

def main(n: int):
    # 生成测试数据：根据规模 n 生成 m
    # 这里简单设置 m 为 0 到 10^9 之间的随机整数
    m = random.randint(0, 10**9)

    if n < 27:
        print(m % (2 ** n))
    else:
        print(m)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要修改
    main(10)
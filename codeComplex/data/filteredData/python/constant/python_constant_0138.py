import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里简单设计为：a 和 b 在 [1, 10^n] 范围内随机取值
    if n <= 0:
        n = 1
    upper = 10 ** n
    a = random.randint(1, upper)
    b = random.randint(1, upper)

    res = 0
    temp = 0

    if a % b == 0:
        print(int(a / b))
    else:
        while b != 0:
            res += a // b
            a %= b
            temp = a
            a = b
            b = temp
        print(res)


if __name__ == "__main__":
    # 示例：用 n=3 运行一次
    main(3)
import random

def main(n: int):
    # 生成测试数据：a, b 范围 [0, 2^n - 1]
    if n <= 0:
        a = 0
        b = 0
    else:
        upper = (1 << n) - 1
        a = random.randint(0, upper)
        b = random.randint(0, upper)

    if a == b:
        print(0)
    else:
        x = a ^ b
        c = 0
        while x:
            x //= 2
            c += 1
        print(2**c - 1)


if __name__ == "__main__":
    # 可自行修改 n 的默认测试规模
    main(10)
import random

def main(n: int):
    # 根据规模 n 生成两个整数 a, b
    # 这里示例为：a, b 在 [0, 2^n - 1] 范围内随机生成
    if n <= 0:
        a, b = 0, 0
    else:
        upper = (1 << n) - 1
        a = random.randint(0, upper)
        b = random.randint(0, upper)

    s = a ^ b
    cnt = 0
    while s != 0:
        s = int(s / 2)
        cnt = cnt + 1
    print((2 ** cnt) - 1)

if __name__ == "__main__":
    # 示例：传入规模 n = 10
    main(10)
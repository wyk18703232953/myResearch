import random

def main(n: int):
    # 根据规模 n 生成两个整数 a, b
    # 这里假设规模 n 表示数字的大致位数上界
    # 范围设为 [0, 2^n - 1]，n 过大时注意性能
    if n <= 0:
        a = 0
        b = 0
    else:
        upper = (1 << n) - 1
        a = random.randint(0, upper)
        b = random.randint(0, upper)

    # 原逻辑
    s = a ^ b
    cnt = 0
    while s != 0:
        s = int(s / 2)
        cnt = cnt + 1
    result = (2 ** cnt) - 1

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
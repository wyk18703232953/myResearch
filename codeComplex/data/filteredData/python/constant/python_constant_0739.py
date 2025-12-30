import random

def main(n: int):
    # 根据规模 n 生成一个整数 a，可按需要调整范围
    # 这里简单设定 a 在 [1, n] 之间
    if n <= 0:
        return

    a = random.randint(1, n)
    print(a**2 + (a - 1)**2)


if __name__ == "__main__":
    # 示例：可在此处指定规模 n
    main(10)
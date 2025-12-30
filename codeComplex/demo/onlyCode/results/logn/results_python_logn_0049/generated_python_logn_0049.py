import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里使用 n 的位数上限来生成 a, b
    # 例如 n=10 -> a,b < 2^10
    if n <= 0:
        a = 0
        b = 0
    else:
        upper = 1 << n  # 2^n
        a = random.randint(0, upper - 1)
        b = random.randint(0, upper - 1)

    x = a ^ b
    ans = 1
    while x > 0:
        x //= 2
        ans *= 2

    print(ans - 1)

if __name__ == "__main__":
    # 示例：使用 n=10
    main(10)
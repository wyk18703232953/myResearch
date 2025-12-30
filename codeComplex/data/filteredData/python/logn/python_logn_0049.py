import random

def main(n):
    # 生成规模为 n 的测试数据，这里用 n 作为 a 的上界
    # 确保上界至少为 1，避免 random.randint(0, 0) 出错
    upper = max(1, n)
    a = random.randint(0, upper)
    b = random.randint(0, upper)

    x = a ^ b
    ans = 1
    while x > 0:
        x //= 2
        ans *= 2

    print(ans - 1)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)
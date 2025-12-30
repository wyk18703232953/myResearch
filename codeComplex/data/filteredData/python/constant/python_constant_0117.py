import random

def main(n):
    # 根据规模 n 生成一个测试整数，这里简单地生成 [-10^n, 10^n] 范围内的随机数
    if n <= 0:
        test_value = 0
    else:
        limit = 10 ** n
        test_value = random.randint(-limit, limit)

    x = test_value

    if x >= 0:
        result = x
    else:
        a = int(x / 10)
        b = int(x / 100) * 10 - abs(x) % 10
        result = max(a, b)

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(2)，可按需修改 n 的值
    main(2)
import random

def main(n):
    # 生成一个测试整数：在 [-10**k, 10**k] 范围内，k 与 n 相关
    # 为保证范围合理，这里令 k = max(1, min(9, n))
    k = max(1, min(9, n))
    test_n = random.randint(-10**k, 10**k)

    n = test_n
    if n >= 0:
        print(n)
    else:
        if (n * -1) // 10 == 0:
            print(0)
        else:
            n *= -1
            y = n // 10
            z = n % 10
            x = y // 10
            x *= 10
            x += z
            x *= -1
            y *= -1
            if x >= y:
                print(x)
            else:
                print(y)


if __name__ == "__main__":
    # 示例：调用 main，指定规模 n
    main(5)
import random

def main(n):
    # 根据规模 n 生成一个测试整数（位数不超过 n）
    # 约定：当 n <= 0 时，使用一个固定示例
    if n <= 0:
        test_value = "-123"
    else:
        # 位数在 1 到 n 之间
        length = random.randint(1, n)
        # 决定正负号
        sign = random.choice([-1, 1])
        # 第一位不能为 0（如果长度 > 1）
        first_digit = random.randint(1, 9)
        digits = [str(first_digit)]
        # 后续位可以为 0-9
        for _ in range(length - 1):
            digits.append(str(random.randint(0, 9)))
        test_value = str(sign * int("".join(digits)))

    # 以下是原逻辑的改写（用 test_value 代替 input()）
    s = test_value  # 原来的 n 是字符串，这里用 s 表示
    x = int(s)

    if x > 0:
        print(s)
    elif -9 <= x <= 0:
        print(0)
    else:
        a = (-x) // 10
        b = ((-x) // 100) * 10 + int(s[-1])
        print(max(-a, -b))

if __name__ == "__main__":
    # 示例：调用 main，规模设为 5
    main(5)
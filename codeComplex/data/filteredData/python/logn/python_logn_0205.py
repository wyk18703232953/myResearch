import random

def summing(number: int) -> int:
    summa = 0
    while number > 0:
        summa += number % 10
        number = number // 10
    return summa


def result(n: int, s: int) -> int:
    z = min(s, n)
    while z <= n and z - summing(z) < s:
        z += 1
    return n - z + 1


def main(n: int):
    """
    n 作为规模参数，用于生成测试数据。
    原程序输入为两个整数 a, b，含义为：
    result(a, b)
    这里用 n 控制 a 的大小上界，并生成 b 作为相对较小的参数。
    """
    # 生成测试数据：
    # a 在 [1, n] 内，b 在 [0, a] 内（包含 0 的情况）
    if n < 1:
        a = 1
    else:
        a = random.randint(1, n)
    b = random.randint(0, a)

    ans = result(a, b)
    print(ans)


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(10**6)
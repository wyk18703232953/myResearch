from math import log2
import sys


def main(n: int):
    out = sys.stdout

    if n == 3:
        out.write("1 1 3")
        return

    tmp = n
    current = 1
    while n != 1:
        if n % 2 != 0:
            z = (n // 2) + 1

        else:
            z = n // 2
        for _ in range(z):
            out.write(str(current) + ' ')
        n -= z
        current *= 2

    step = int(log2(tmp))
    if tmp % 2 ** (step - 1) == 0:
        out.write(str(tmp))

    else:
        q = 2 ** (step - 1)
        ans = 0
        for i in range(1, 1000):
            if q * i <= tmp:
                ans = max(ans, q * i)

            else:
                break
        out.write(str(ans))


if __name__ == "__main__":
    # 这里根据需要生成测试数据并调用 main(n)
    # 示例：使用一个固定规模 n 进行测试
    test_n = 10
    main(test_n)
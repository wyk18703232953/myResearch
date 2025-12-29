import math
import random

def main(n: int):
    # 这里根据 n 生成测试数据，本题原逻辑只需要一个整数 n
    # 所以直接使用传入的 n 作为规模参数

    # 原始逻辑从这里开始
    if n == 1:
        print(1)
        return

    if n == 2:
        print(1, 2)
        return

    if n == 3:
        print(1, 1, 3)
        return

    ar = [0] * 30

    for i in range(30):
        ar[i] = n // (2 ** i) - n // (2 ** (i + 1))

    sd = 0
    for i in range(30):
        if sd == n - 1:
            if n == (2 ** i):
                print(2 ** i)
            else:
                print(n - n % (2 ** (i - 1)))
            return
        for _ in range(ar[i]):
            print(2 ** i, end=' ')
            sd += 1

# 示例：直接调用 main(10) 进行演示
if __name__ == "__main__":
    main(10)
import random
import math

def main(n):
    # 生成测试数据：r 为 1~10 的随机整数，x 为 n 个 -10*n~10*n 内的随机整数
    r = random.randint(1, 10)
    x = [random.randint(-10 * n, 10 * n) for _ in range(n)]

    y = [r] * n
    for i in range(n):
        for j in range(i):
            if not (abs(x[i] - x[j]) > 2 * r):
                y[i] = max(
                    y[i],
                    math.sqrt(4 * r ** 2 - (x[i] - x[j]) ** 2) + y[j]
                )
    for val in y:
        print(val, end=' ')

if __name__ == "__main__":
    # 示例：规模为 5，可按需修改
    main(5)
from copy import copy
import random

def main(n):
    # 生成规模为 n 的测试数据，这里生成 0~100 的随机整数
    a = [random.randint(0, 100) for _ in range(n)]

    ans = 0
    for i in range(n):
        b = copy(a)
        b[i] = 0

        for j in range(1, n + 1):
            b[(i + j) % n] += (a[i] - 1) // n + ((a[i] - 1) % n + 1 > j - 1)

        ans = max(ans, sum(el * (el % 2 == 0) for el in b))

    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 14 运行（与原题规模一致）
    main(14)
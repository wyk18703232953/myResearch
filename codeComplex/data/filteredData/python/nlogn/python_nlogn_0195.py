import random
from collections import defaultdict as dc

def main(n):
    # 生成测试数据：随机生成长度为 n 的整数数组 l
    # 你也可以按需要修改数据生成方式
    l = [random.randint(0, 10) for _ in range(n)]

    x = dc(int)
    y = dc(int)
    z = dc(int)
    p = dc(int)
    q = dc(int)
    r = dc(int)

    x[l[-1]] += 1
    y[l[-1]] += 1
    z[l[-1]] += 1

    for i in range(n - 2, -1, -1):
        p[i] = x[l[i]]
        q[i] = y[l[i] + 1]
        r[i] = z[l[i] - 1]
        x[l[i]] += 1
        y[l[i]] += 1
        z[l[i]] += 1

    x_arr = [0] * n
    for i in range(n - 2, -1, -1):
        x_arr[i] = l[i + 1] + x_arr[i + 1]

    s = 0
    for i in range(n - 2, -1, -1):
        c = x_arr[i] - (p[i] * l[i]) - (q[i] * (l[i] + 1)) - (r[i] * (l[i] - 1))
        d = n - i - 1 - p[i] - q[i] - r[i]
        e = c - l[i] * d
        s += e

    print(s)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
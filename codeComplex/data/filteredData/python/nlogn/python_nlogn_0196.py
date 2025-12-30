from collections import defaultdict as di
import random

def main(n):
    # 生成测试数据：长度为 n 的整数数组 a
    # 这里生成 1 到 n 之间的随机整数，可根据需要调整范围
    a = [random.randint(1, n) for _ in range(n)]

    d = di(int)
    res, s = 0, 0
    for i in range(n):
        res += a[i] * i - s - d[a[i] - 1] + d[a[i] + 1]
        s += a[i]
        d[a[i]] += 1

    print(res)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)
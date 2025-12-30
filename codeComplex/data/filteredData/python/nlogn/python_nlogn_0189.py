import random

def main(n: int):
    # 生成测试数据：长度为 n 的数组，元素为 1..n 的随机整数
    arr = [random.randint(1, n) for _ in range(n)]

    d = {}
    rawsum = 0
    a = n - 1
    b = 1

    for i in range(n):
        if i == 0:
            rawsum = rawsum - (arr[i] * a)
            a -= 1
        elif i == n - 1:
            rawsum = rawsum + (arr[i] * b)
            b += 1
        else:
            rawsum = rawsum + (arr[i] * b)
            rawsum = rawsum - (arr[i] * a)
            a -= 1
            b += 1

    i = n - 1
    while i >= 0:
        if d.get(arr[i]) is None:
            d[arr[i]] = 1
        else:
            d[arr[i]] = d[arr[i]] + 1

        s = arr[i] - 1
        g = arr[i] + 1

        if d.get(s) is not None:
            rawsum += d[s]
        if d.get(g) is not None:
            rawsum -= d[g]

        i -= 1

    print(rawsum)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
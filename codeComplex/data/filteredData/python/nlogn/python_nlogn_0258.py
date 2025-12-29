import random

def main(n: int):
    # 1. 生成测试数据：n 个区间 [l, r]，下标从 1 到 n
    #   这里简单地生成：l 在 [1, 2n] 之间，r 在 [l, l+2n] 之间
    a = []
    for i in range(n):
        l = random.randint(1, 2 * n)
        r = random.randint(l, l + 2 * n)
        a.append([l, r, i + 1])

    # 2. 按原逻辑处理
    a.sort(key=lambda x: (x[0], -x[1]))
    r = 0
    iid = 0
    f = 1
    for i in range(n):
        if r >= a[i][1]:
            f = 0
            print(a[i][2], a[iid][2])
            break
        else:
            r = a[i][1]
            iid = i
    if f:
        print("-1 -1")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
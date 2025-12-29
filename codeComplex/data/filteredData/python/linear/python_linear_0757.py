import random

def main(n: int):
    # 生成测试数据：n 个整数，范围可自行调整
    # 这里设为 [-10^9, 10^9]
    arr = [random.randint(-10**9, 10**9) for _ in range(n)]

    a = []
    for i in arr:
        if abs(-i - 1) > abs(i):
            a.append(-i - 1)
        else:
            a.append(i)

    c = 0
    for i in a:
        if i < 0:
            c += 1

    if c % 2:
        me = 0
        for i in range(len(a)):
            if a[i] < a[me]:
                me = i
        a[me] = -a[me] - 1

    print(*a)


if __name__ == "__main__":
    # 示例调用，n 可按需修改
    main(5)
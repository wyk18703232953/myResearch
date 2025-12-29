import random

def main(n: int):
    # 生成测试数据 a：长度为 n 的整数数组
    # 这里示例生成 0~10 之间的随机整数
    a = [random.randint(0, 10) for _ in range(n)]

    khat = [0] * n
    ted = 0
    khat[0] = 1

    # 正向遍历
    for i in range(1, n):
        khat[i] = max(khat[i - 1], a[i] + 1)

    # 反向遍历
    for i in range(n - 2, -1, -1):
        if khat[i] < khat[i + 1] - 1:
            khat[i] = khat[i + 1] - 1
        ted += khat[i] - (a[i] + 1)

    ted += khat[n - 1] - (a[n - 1] + 1)

    print(ted)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
import random

def main(n):
    # 生成测试数据：k 在 [1, 2*n] 范围内随机选取
    if n <= 0:
        return

    k = random.randint(1, 2 * n)

    # 原逻辑
    if 2 * n - 1 < k:
        print(0)
    elif k <= n + 1:
        if k % 2:
            print(k // 2)
        else:
            print(k // 2 - 1)
    else:
        t1 = k - n
        if k % 2 == 0:
            print(k // 2 - t1)
        else:
            print(k // 2 - t1 + 1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
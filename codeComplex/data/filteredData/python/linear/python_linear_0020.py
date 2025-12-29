import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组
    # 为保证逻辑有意义，尽量混合奇偶数
    arr = [random.randint(0, 100) for _ in range(n)]

    codd = 0
    ceven = 0
    ptodd = -1
    pteven = -1

    for i in range(n):
        if arr[i] % 2 == 0:
            ceven += 1
            pteven = i
        else:
            codd += 1
            ptodd = i

    if ceven == 1:
        print(pteven + 1)
    else:
        print(ptodd + 1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
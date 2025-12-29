import random

def main(n: int):
    # 生成测试数据：长度为 n 的随机整数列表，范围 1~100
    l = [random.randint(1, 100) for _ in range(n)]

    c1 = 0  # 偶数计数
    c2 = 0  # 奇数计数
    for i in l:
        if i % 2 == 0:
            c1 += 1
        else:
            c2 += 1

    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            lasteven = i
            break

    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 != 0:
            lastodd = i
            break

    if c1 == 1:
        print(lasteven + 1)
    else:
        print(lastodd + 1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
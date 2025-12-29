import random

def main(n):
    # 生成测试数据：n个非负整数，这里设定范围为[0, 10^6]
    # 可根据需要调整数据分布
    a = [random.randint(0, 10**6) for _ in range(n)]

    a.sort()
    lose = False
    pair = False

    for i in range(n - 1):
        if a[i] == a[i + 1] == 0:
            lose = True
        if a[i] == a[i + 1]:
            if pair:
                lose = True
            pair = True
            if i >= 1 and a[i] == a[i - 1] + 1:
                lose = True

    if lose:
        print("cslnb")
    else:
        eventual = n * (n - 1) // 2
        curr = sum(a)
        if (curr - eventual) % 2 == 0:
            print("cslnb")
        else:
            print("sjfnb")


# 示例：调用 main(5)
if __name__ == "__main__":
    main(5)
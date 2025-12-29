import random

def main(n: int):
    # 根据 n 生成测试数据：生成 n 个非负整数
    # 这里选择范围 [0, 2n]，可按需要调整
    a = [random.randint(0, 2 * n) for _ in range(n)]

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


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
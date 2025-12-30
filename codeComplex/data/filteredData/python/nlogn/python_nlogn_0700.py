import random

def main(n: int):
    # 1. 生成测试数据：长度为 n 的整数数组 a
    #   这里生成非负整数，范围可按需调整
    a = [random.randint(0, 10**6) for _ in range(n)]

    # 2. 原始逻辑开始
    a.sort()

    if n == 1:
        if a[0] % 2 == 1:
            v = True
        else:
            v = False
    else:
        v = True
        c = 0
        j = -1
        for i in range(0, n - 1):
            if a[i] == a[i + 1]:
                c = c + 1
                j = i
        if c > 1:
            v = False
        elif c == 1:
            if a[j] == 0:
                v = False
            if j > 0:
                if a[j - 1] + 1 == a[j]:
                    v = False
        if (sum(a) - (n * (n - 1)) // 2) % 2 == 0:
            v = False

    if v:
        print("sjfnb")
    else:
        print("cslnb")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
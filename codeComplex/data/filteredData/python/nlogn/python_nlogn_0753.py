import random
import sys

def main(n: int):
    # 生成测试数据：n个非负整数，范围可根据需要调整
    # 这里生成 0 ~ 10^6 之间的随机整数
    a = [random.randint(0, 10**6) for _ in range(n)]

    a.sort()
    t = 0
    for i in range(1, n):
        t += a[i] == a[i - 1]
    if t >= 2:
        print("cslnb")
        return
    if t:
        for i in range(n - 1):
            if a[i] == a[i + 1]:
                if a[i] and (i == 0 or a[i] != a[i - 1] + 1):
                    a[i] -= 1
                    break
                else:
                    print("cslnb")
                    return
    print(["cslnb", "sjfnb"][(sum(a) - t - n * (n - 1) // 2) & 1])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
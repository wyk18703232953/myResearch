import random

def main(n: int):
    # 生成测试数据：n 个整数，范围可根据需要调整
    # 这里生成在 [-10^9, 10^9] 范围内的随机整数
    a = [-1] + [random.randint(-10**9, 10**9) for _ in range(n)]

    s = set()
    s.add(-1)
    a.sort()
    count, add = 0, 0
    flag = 0

    for i in range(1, n + 1):
        if a[i] in s and a[i] - 1 in s:
            flag = 1
            break
        if a[i] in s:
            add += 1
        if add == 2:
            flag = 1
            break
        s.add(a[i])
        count += a[i] - (i - 1)

    if flag == 0 and count % 2 == 1:
        print("sjfnb")
    else:
        print("cslnb")


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)
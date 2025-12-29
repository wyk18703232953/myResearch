import random

def main(n):
    # 生成测试数据：n 和 m，随后生成长度为 n 的数组 a
    # 可根据需要自定义生成逻辑
    m = random.randint(1, max(1, n))  # m 无实际参与后续逻辑，保留形式
    # 生成 n 个正整数，范围可调
    a = [random.randint(1, max(2 * n, 10)) for _ in range(n)]

    s = sum(a)
    need = 0
    a.sort()
    j = 1
    flag = 0
    k = max(a)

    if n == 1:
        print(0)
        return

    for i in range(n):
        if a[i] < j:
            flag = 1
        else:
            flag = 0

        if a[i] == 1:
            need += 1
        elif a[i] >= j and i != n - 1:
            need += 1
        elif a[i] >= j and i == n - 1 and j <= k:
            need += k - j + 1
        else:
            need += 1

        if flag != 1:
            j += 1

    print(s - need)


if __name__ == "__main__":
    # 示例运行：可按需修改 n
    main(5)
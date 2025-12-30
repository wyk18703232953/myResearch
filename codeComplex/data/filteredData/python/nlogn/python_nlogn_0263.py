import random

def main(n):
    # 生成测试数据：n 行，每行两个整数 (例如在 1~100 范围内)
    a = []
    for i in range(n):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        a.append([x, y, i + 1])  # 附带原始编号

    # 原逻辑
    a.sort(key=lambda e: e[0])
    f = 0
    for i in range(n - 1):
        if a[i][0] == a[i + 1][0]:
            if a[i][1] >= a[i + 1][1]:
                print(a[i + 1][2], a[i][2])
            else:
                print(a[i][2], a[i + 1][2])
            f = 1
            break
        if a[i][1] >= a[i + 1][1]:
            f = 1
            print(a[i + 1][2], a[i][2])
            break
    if f == 0:
        print(-1, -1)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)
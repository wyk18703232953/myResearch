import random

def main(n):
    # 生成测试数据：n个非负整数
    # 这里生成0到2n范围内的随机数，可根据需要调整
    a = [random.randint(0, 2 * n) for _ in range(n)]

    a.sort()
    flag = 0
    index = -1
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            if flag == 1:
                flag = 2
                break
            flag = 1
            index = i
            if i + 2 < n and a[i + 1] == a[i + 2]:
                flag = 2
                break
            elif i > 0 and a[i - 1] == a[i] - 1:
                flag = 2
                break

    if flag == 2:
        print("cslnb")
    elif flag == 1 and a[index] == 0:
        print("cslnb")
    else:
        moves = 0
        for i in range(n):
            if a[i] == i:
                continue
            elif a[i] < i:
                continue
            else:
                moves += (a[i] - i)
        if moves % 2 == 0:
            print("cslnb")
        else:
            print("sjfnb")


if __name__ == "__main__":
    # 示例：调用 main，规模为 5
    main(5)
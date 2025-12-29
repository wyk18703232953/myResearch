import random

def main(n):
    # 生成测试数据：n个整数，范围可根据需要调整
    # 这里生成 [-10^9, 10^9] 区间内的随机整数
    l = [random.randint(-10**9, 10**9) for _ in range(n)]

    m = 0
    for i in range(n):
        if l[i] >= 0:
            l[i] = -l[i] - 1

    for i in range(n):
        if l[i] < 0:
            m += 1

    if m % 2 == 0:
        for i in range(n):
            print(l[i], end=" ")
    else:
        maksi = -10**18
        mk = 0
        for i in range(n):
            if abs(l[i]) > maksi:
                maksi = abs(l[i])
                mk = i
        l[mk] = -l[mk] - 1
        for i in range(n):
            print(l[i], end=" ")

if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)
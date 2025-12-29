import random

def main(n):
    # 1. 生成测试数据：n 个随机整数
    #   范围可按需要调整，这里使用 [-10^9, 10^9]
    arr = [random.randint(-10**9, 10**9) for _ in range(n)]

    unique = set(arr)
    poss = False

    # 尝试找到长度为 3 的序列
    for i in arr:
        for j in range(32):
            d = 1 << j
            if (i + d) in unique and (i - d) in unique:
                print(3)
                print(i, i + d, i - d)
                poss = True
                break
        if poss:
            break

    if poss:
        return

    # 尝试找到长度为 2 的序列
    for i in arr:
        for j in range(32):
            d = 1 << j
            if (i + d) in unique:
                print(2)
                print(i, i + d)
                poss = True
                break
        if poss:
            break

    if poss:
        return

    # 否则输出长度为 1 的序列
    print(1)
    print(arr[0])


if __name__ == "__main__":
    # 示例：调用 main，n 可自行修改
    main(10)
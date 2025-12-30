import random

def main(n: int):
    # 生成测试数据：n 个随机整数，范围可自行调整
    l1 = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 原逻辑开始
    l2 = []
    for i in l1:
        l2.append(int(i))
    l1 = set(l2)
    l1 = list(l1)
    for i in range(0, len(l1)):
        for j in range(i + 1, len(l1)):
            if l1[i] > l1[j]:
                temp = l1[j]
                l1[j] = l1[i]
                l1[i] = temp
    if len(l1) > 1:
        print(l1[1])
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
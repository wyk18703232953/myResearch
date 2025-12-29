import random

def main(n: int):
    # 生成测试数据：n 个随机整数（可为正负，范围可调）
    # 你也可以改成固定序列或其他分布
    l1 = [random.randint(-1000, 1000) for _ in range(n)]

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
    # 示例：规模为 10
    main(10)
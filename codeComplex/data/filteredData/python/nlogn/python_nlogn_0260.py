import random

def main(n):
    # 生成测试数据：n 行 (a, b)，这里用随机整数示例
    # 可按需要调整随机范围或生成规则
    data = []
    for _ in range(n):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        data.append((a, b))

    l = []
    for idx, (a, b) in enumerate(data, start=1):
        l.append((a, -b, idx))

    l.sort()

    for i in range(1, n):
        if l[i][1] >= l[i - 1][1]:
            print(l[i][2], l[i - 1][2])
            break
    else:
        print(-1, -1)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)
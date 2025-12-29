import random

def main(n: int):
    # 生成测试数据：n 行，每行 1~5 个随机整数
    data = []
    for _ in range(n):
        k = random.randint(1, 5)              # 每行的整数个数
        row = [random.randint(-100, 100) for _ in range(k)]
        data.append(row)

    # 原逻辑开始
    l = []
    for row in data:
        l.append(sum(row))

    m = l[0]
    l.sort(reverse=True)
    for i in range(len(l)):
        if m == l[i]:
            print(i + 1)
            break

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)
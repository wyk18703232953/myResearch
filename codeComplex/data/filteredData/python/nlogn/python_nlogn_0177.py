import random

def main(n: int):
    # 生成测试数据：n 行，每行两个整数 [x, r]
    # x 为中心位置，r 为半径，保证为非负整数
    # 这里示例生成范围：x ∈ [0, 10*n], r ∈ [0, 5*n]
    ls = []
    for _ in range(n):
        x = random.randint(0, 10 * n)
        r = random.randint(0, 5 * n)
        ls.append([x, r])

    # 以下是原逻辑
    lsr = [[max(ls[i][0] - ls[i][1], 0), ls[i][0] + ls[i][1]] for i in range(n)]
    lsr.sort(key=lambda x: x[1])
    idx = 0
    ans = 0

    for l in lsr:
        if idx <= l[0]:
            idx = l[1]
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例运行
    main(10)
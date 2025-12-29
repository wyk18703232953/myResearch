import random

def main(n):
    # 生成测试数据
    # 分数上下界、难度差下界可自行调整规则
    l = 10
    r = 1000
    x = 5

    # 生成 n 个题目难度，保证有一定范围
    C = [random.randint(1, 100) for _ in range(n)]

    # 按原逻辑计算答案
    C.sort()
    ANS = 0
    for mask in range(1 << n):
        selected = []
        for j in range(n):
            if mask & (1 << j):
                selected.append(C[j])

        if len(selected) < 2:
            continue
        total = sum(selected)
        if not (l <= total <= r):
            continue
        if selected[-1] - selected[0] < x:
            continue
        ANS += 1

    print(ANS)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)
import random

def main(n):
    # 生成测试数据
    # p: n个元素的难度值
    # l, r: 允许的难度和区间
    # d: 最小难度差
    random.seed(0)  # 固定种子，保证可复现
    p = [random.randint(1, 20) for _ in range(n)]
    total_sum = sum(p)
    l = random.randint(0, total_sum // 2)
    r = random.randint(l, total_sum)
    d = random.randint(0, max(p) - min(p) if n > 1 else 0)

    t = 0
    for v in range(1, 2 ** n):  # 原程序从0开始，空集不可能满足 max-min>=d，跳过也可
        s = []
        for i in range(n):
            if v & (1 << i):
                s.append(p[i])
        if s:
            s_sum = sum(s)
            if l <= s_sum <= r and max(s) - min(s) >= d:
                t += 1

    print(t)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)
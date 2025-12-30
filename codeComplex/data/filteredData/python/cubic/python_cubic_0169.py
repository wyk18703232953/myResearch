import random

def main(n: int) -> int:
    # 1. 生成规模为 n 的测试数据 b
    # 根据原代码逻辑，b 是一组整数序列，这里生成 1~3 之间的随机整数
    random.seed(0)
    b = [random.randint(1, 3) for _ in range(n)]

    # 2. 原始算法逻辑
    d = [[-1 if i != j else b[i] for i in range(n)] for j in range(n)]
    for l in range(1, n):
        for s in range(n - l):
            e = s + l
            for m in range(s, e):
                if d[s][m] == d[m + 1][e] and d[s][m] != -1:
                    d[s][e] = d[s][m] + 1
    a = [1]
    for e in range(1, n):
        t = 4096
        for s in range(e + 1):
            if d[s][e] != -1:
                t = min(t, ((a[s - 1] + 1) if s > 0 else a[s]))
        a.append(t)
    # 输出与原程序一致的结果：最优值 a[-1]
    print(a[-1])
    return a[-1]


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)
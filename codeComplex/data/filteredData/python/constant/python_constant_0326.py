import random

def score(l):
    return sum(x * (x % 2 == 0) for x in l)

def main(n):
    # 生成规模为 n 的测试数据，这里生成 0~100 的随机整数
    ns = [random.randint(0, 100) for _ in range(n)]

    res = 0
    for i in range(n):
        l = list(ns)
        base = l[i] // n
        rem = l[i] % n
        for j in range(n - 1):
            idx = (i + 1 + j) % n
            l[idx] += base + (1 if (j + 1) <= rem else 0)
        l[i] = base
        res = max(res, score(l))

    print(res)

if __name__ == "__main__":
    # 示例调用：n 对应原程序中的 14
    main(14)
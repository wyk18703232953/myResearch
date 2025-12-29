import random

def main(n):
    # 生成测试数据：n, l, r, d 以及长度为 n 的数组 op
    # 这里给出一种合理的生成方式，可按需要调整
    # 假设 op 中的数在 [1, 100] 之间
    op = [random.randint(1, 100) for _ in range(n)]
    total_sum = sum(op)
    # l, r 在 [0, total_sum] 范围内，且 l <= r
    l = random.randint(0, total_sum // 2)
    r = random.randint(l, total_sum)
    # d 在 [0, max(op) - min(op)] 范围内
    d = random.randint(0, max(op) - min(op) if n > 0 else 0)

    # 逻辑与原程序一致
    c = 0
    for i in range(2, 2 ** n):
        s = 0
        k = 0
        maxx = 0
        minn = 1000001
        x = bin(i)[2:]
        x = '0' * (n - len(x)) + x
        for j in range(n):
            if x[j] == '1':
                s += op[j]
                k += 1
                if maxx < op[j]:
                    maxx = op[j]
                if op[j] < minn:
                    minn = op[j]
        if l <= s <= r and maxx - minn >= d and k >= 2:
            c += 1

    print(c)
    return c

if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(5)
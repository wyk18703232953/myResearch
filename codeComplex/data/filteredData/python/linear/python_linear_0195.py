import random

def main(n):
    # 根据规模 n 生成测试数据
    # 生成参数 a, b, c, t
    # 约束：0 <= l[i] <= t，保证原逻辑中的 k = t - l[i] 为非负
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    # t 至少要不小于最大 l[i]，先生成 l，再设 t
    l = [random.randint(0, 100) for _ in range(n)]
    t = max(l) + random.randint(0, 50)

    if c > b:
        r = 0
        for i in l:
            k = t - i
            k *= (c - b)
            r += k
        print(a * n + r)
    else:
        print(a * n)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)
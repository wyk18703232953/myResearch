import random

def main(n):
    # 生成测试数据
    # 约束：k >= 1，n >= 2（原逻辑中有遍历到 n-1）
    if n < 2:
        raise ValueError("n 必须 >= 2")

    k = random.randint(1, max(1, n))          # 随机生成 k
    lst = [random.randint(0, 1000) for _ in range(n)]  # 随机生成数组

    # 原始逻辑
    s = sum(lst)
    s2 = 0
    m = 0
    for i in range(n - 1):
        s2 += lst[i]
        s -= lst[i]
        if (s2 % k) + (s % k) > m:
            m = (s2 % k) + (s % k)

    # 输出结果（可根据需要返回或打印）
    print(m)
    return m

if __name__ == "__main__":
    # 示例运行：可修改 n 以测试不同规模
    main(10)
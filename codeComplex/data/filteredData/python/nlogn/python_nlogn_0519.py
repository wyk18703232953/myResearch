import random

def main(n):
    # 生成测试数据：
    # 原题逻辑：a中要有重复元素，才能进入 b 列表进行比较
    # 这里构造一个长度为 n 的数组，其中包含一些重复数
    if n < 4:
        n = 4  # 保证有机会出现至少两对相同值

    # 随机生成基础数值集合
    base_values = [random.randint(1, 10**4) for _ in range(max(2, n // 4))]
    # 构造含重复元素的数组
    a = []
    for v in base_values:
        a.extend([v, v])  # 每个值至少两次
        if len(a) >= n:
            break
    # 若长度不足，再填充一些随机值
    while len(a) < n:
        a.append(random.randint(1, 10**4))
    random.shuffle(a)

    # 以下为原逻辑封装
    b = []
    res_a, res_b = 1, 10**18

    a.sort()
    i = 0
    while i < n - 1:
        if a[i] == a[i + 1]:
            b.append(a[i])
            i += 1
        i += 1

    def p2s(x, y):
        return (x + y) ** 2 / (x * y)

    # 若重复元素不足两种，按原代码逻辑，循环不会更新 res_a/res_b
    for i in range(len(b) - 1):
        if p2s(res_a, res_b) > p2s(b[i], b[i + 1]):
            res_a, res_b = b[i], b[i + 1]

    print(res_a, res_a, res_b, res_b)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次运行
    main(10)
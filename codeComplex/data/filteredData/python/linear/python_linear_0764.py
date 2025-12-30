def main(n):
    """
    n 用作规模参数，这里约定：
    - 数组长度 = n
    - 查询次数 q = n
    - 数组 a 为 1..n 的简单递增序列（可按需改造为更复杂的随机/构造数据）。
    """
    import random

    # 1. 生成测试数据
    # 数组长度为 n
    N = n
    # 查询次数也设为 n
    q = n

    # 示例1：递增数组（保证最大值在末尾）
    # a = list(range(1, N + 1))

    # 示例2：随机数组（保证非空）
    a = [random.randint(1, 10**9) for _ in range(N)]

    # 示例3：也可以保证最大值不在首位，防止 t = 0 退化
    # 这里简单做一下：如果最大值在 0 位置就和最后一个交换
    max_idx = max(range(N), key=lambda i: a[i])
    if max_idx == 0 and N > 1:
        a[0], a[-1] = a[-1], a[0]

    # 生成查询：覆盖 1..N，然后一些更大的值
    queries = []
    for i in range(1, q + 1):
        if i <= N + 5:
            queries.append(i)
        else:
            # 一些更大的查询
            queries.append(i * 2)

    # 2. 将原逻辑封装，无 input()

    n = N  # 与原代码中变量名对齐

    max_a = max(a)
    t = a.index(max_a)
    last = a[0]
    Lis = []
    tmp = []

    for i in range(1, t + 1):
        Lis.append((last, a[i]))
        if last < a[i]:
            tmp.append(last)
            last = a[i]
        else:
            tmp.append(a[i])

    anslist = a[t + 1:] + tmp

    # 3. 处理查询并输出（这里直接 print，按原题行为）
    for tm in queries:
        if 1 <= tm <= t:
            print(Lis[tm - 1][0], Lis[tm - 1][1])
        else:
            if len(anslist) == 0:
                # 极端情况：t 为最后一个下标且没有 anslist，
                # 对于这类题一般不会出现；防御性处理一下。
                print(max_a, max_a)
            else:
                print(max_a, anslist[(tm - t - 1) % len(anslist)])


if __name__ == "__main__":
    # 示例调用：规模设为 10
    main(10)
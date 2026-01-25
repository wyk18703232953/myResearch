def main(n):
    # 将 n 解释为数组长度，保证至少 2
    n = max(2, int(n))

    # 构造确定性的初始数组和查询
    # 数组：简单递增 1..n
    nums = list(range(1, n + 1))
    # 查询数 q 和查询序列，覆盖前缀和循环区间
    q = n
    queries = list(range(1, q + 1))

    # 保留一份工作副本
    work = nums[:]

    m = max(work)
    ab = []
    # 模拟直到最大元素到达队首
    while work[0] < m:
        ab.append([work[0], work[1]])
        # 保持原有算法逻辑：比较前两个元素并旋转
        if work[0] > work[1]:
            # 把第二个元素移到末尾
            work.append(work.pop(1))
        else:
            # 把第一个元素移到末尾
            work.append(work.pop(0))

    # 回答查询，收集输出以便实验时可忽略打印开销
    outputs = []
    for mj in queries:
        if mj <= len(ab):
            pair = ab[mj - 1]
            a, b = str(pair[0]), str(pair[1])
        else:
            idx = (mj - len(ab) - 1) % (len(work) - 1) + 1
            pair = (m, work[idx])
            a, b = str(pair[0]), str(pair[1])
        outputs.append(a + " " + b)

    # 为了保持行为可观察，这里打印结果
    for line in outputs:
        print(line)

    return outputs


if __name__ == "__main__":
    # 示例：使用 n=10 作为输入规模
    main(10)
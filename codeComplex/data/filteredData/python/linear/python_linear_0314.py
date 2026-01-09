def main(n):
    from collections import deque

    # 映射输入结构：
    # 原程序：读取 n, m 和一个长度为 n 的数组 arr
    # 在实验版本中：给定规模参数 n
    # - 使用 m = max(1, n // 3 + 1) 作为模数规模（随 n 增长）
    # - 生成长度为 n 的 arr，确定性构造：arr[i] = (i * 2 + 3) % (3 * m)
    if n <= 0:
        return

    m = max(1, n // 3 + 1)
    arr = [(i * 2 + 3) % (3 * m) for i in range(n)]

    mods = [0 for _ in range(m)]
    placement = [[] for _ in range(m)]

    for i in range(n):
        r = arr[i] % m
        mods[r] += 1
        placement[r].append(i)

    cnt = 0
    queue = deque()
    target = n // m

    for i in range(2 * m):
        mod = i % m
        if mods[mod] > target:
            excess = mods[mod] - target
            for c in range(excess):
                queue.append([i, placement[mod][c]])
            mods[mod] = target
        elif mods[mod] < target:
            while queue and mods[mod] < target:
                elem, indice = queue.popleft()
                delta = (mod - elem) % m
                mods[mod] += 1
                cnt += delta
                arr[indice] += delta

    # 保持原程序输出结构：先输出操作总数，再输出数组
    # print(cnt)
    pass
    # print(' '.join(str(x) for x in arr))
    pass
if __name__ == "__main__":
    # 示例规模调用，可按需修改或在外部多次调用 main(n)
    main(10)
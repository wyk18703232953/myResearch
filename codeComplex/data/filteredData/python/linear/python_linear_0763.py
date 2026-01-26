def main(n):
    from collections import deque

    # 规模含义：
    # n >= 2：队列长度 = n
    # 令 m = n，用前 n 轮操作作为“查询时间点”
    if n < 2:
        return

    # 构造确定性输入
    # 队列：1, 2, ..., n
    nums = [i for i in range(1, n + 1)]
    mxnum = max(nums)
    d = deque(nums)

    m = n
    qr = [i + 1 for i in range(m)]  # 查询为 1..m

    log = []
    rot = 0

    # 模拟原算法
    while True:
        a = d.popleft()
        b = d.popleft()
        log.append((a, b))
        if a > b:
            a, b = b, a
        d.append(a)
        d.appendleft(b)

        rot += 1
        if b == mxnum:
            break

    # 回答查询
    for q in qr:
        if q <= rot:
            # print(log[q - 1][0], log[q - 1][1])
            pass

        else:
            res = q - rot - 1
            # print(b, d[res % (n - 1) + 1])
            pass
if __name__ == "__main__":
    # 示例：以 n = 5 作为输入规模运行一次
    main(5)
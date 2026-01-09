def main(n):
    if n <= 0:
        return
    # 确定性生成长度为 n 的数组 a，值域控制在 [1, n]
    a = [(i * 2 + 3) % n + 1 for i in range(n)]

    bs = set()
    moves = {}
    # 原代码：moves[a[i]] = list(a[j] for j in range(i % a[i], n, a[i]) if a[j] > a[i])
    # 注意原逻辑根据值 a[i] 存储，而后续 winners 从 n 到 1 遍历按值索引。
    # 为保持行为一致，需保证键覆盖 1..n。若某值未出现在 a 中则其 moves 为空。
    for v in range(1, n + 1):
        moves[v] = []

    for i in range(n):
        step = a[i]
        start = i % step
        li = []
        ai = a[i]
        for j in range(start, n, step):
            if a[j] > ai:
                li.append(a[j])
        moves[a[i]] = li

    winners = {}
    for i in range(n, 0, -1):
        winner = 'A' if any(winners[j] == 'B' for j in moves[i]) else 'B'
        if winner == 'B':
            bs.add(i)
        winners[i] = winner

    result = ''.join(winners[ai] for ai in a)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)
import random

def main(n):
    # 生成测试数据：长度为 n 的数组 a，元素在 [1, n] 内且互不相同
    # 原程序中使用 a[i] 作为字典 moves 的键，并假设键为 1..n
    a = list(range(1, n + 1))
    random.shuffle(a)

    bs = set()
    moves = {}

    # 预处理每个值对应的可到达、更大的值列表
    for i in range(n):
        ai = a[i]
        moves[ai] = [a[j] for j in range(i % ai, n, ai) if a[j] > ai]

    winners = {}
    # 按值从大到小确定每个数字是 A 赢还是 B 赢
    for val in range(n, 0, -1):
        winner = 'A' if any(winners[j] == 'B' for j in moves.get(val, [])) else 'B'
        if winner == 'B':
            bs.add(val)
        winners[val] = winner

    # 输出结果字符串
    res = ''.join(winners[ai] for ai in a)
    print(res)


if __name__ == '__main__':
    # 示例：调用 main(5)
    main(5)
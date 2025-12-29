import random

def main(n: int):
    # 1. 生成测试数据 board，长度为 n，每个元素在 [1, n] 范围内
    # 根据需要可修改生成策略
    random.seed(0)  # 固定种子，便于复现
    board = [random.randint(1, n) for _ in range(n)]

    # 原始逻辑开始
    index = list(range(0, n))
    ascending = [x for _, x in sorted(zip(board, index))]

    winners = n * [""]

    for c in reversed(ascending):
        if board[c] == n:
            winners[c] = "B"
        # going down
        toCheck = c - board[c]
        while toCheck >= 0:
            if winners[toCheck] == "B":
                winners[c] = "A"
            toCheck = toCheck - board[c]
        if winners[c] == "":
            toCheck = c + board[c]
            while toCheck < n:
                if winners[toCheck] == "B":
                    winners[c] = "A"
                toCheck = toCheck + board[c]
        if winners[c] == "":
            winners[c] = "B"

    # 输出结果
    for i in range(n):
        print(winners[i], end="")
    print()


if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)
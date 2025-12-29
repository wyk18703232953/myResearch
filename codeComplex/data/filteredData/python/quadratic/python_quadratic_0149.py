import heapq
import random


def doxor(a, b):
    cnt = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            cnt += a[i][j] ^ b[i][j]
    return cnt


def main(n):
    # 构造棋盘模板 a 和 b
    a, b = [], []
    for i in range(n):
        ai, bi = [], []
        for j in range(n):
            if i % 2 == 0:
                ai.append(j % 2)
                bi.append((j % 2) ^ 1)
            else:
                ai.append((j % 2) ^ 1)
                bi.append(j % 2)
        a.append(ai)
        b.append(bi)

    # 生成 4 个 n x n 的随机棋盘，元素为 0/1
    board = []
    for _ in range(4):
        b0 = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
        board.append(b0)

    a_cnts = []
    b_cnts = []
    for b0 in board:
        heapq.heappush(a_cnts, doxor(b0, a))
        heapq.heappush(b_cnts, doxor(b0, b))

    ans = (
        heapq.heappop(a_cnts)
        + heapq.heappop(a_cnts)
        + heapq.heappop(b_cnts)
        + heapq.heappop(b_cnts)
    )
    print(ans)


if __name__ == "__main__":
    # 示例调用：n 可按需要修改
    main(5)
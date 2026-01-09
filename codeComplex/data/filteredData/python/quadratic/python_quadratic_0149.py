import heapq


def doxor(a, b):
    cnt = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            cnt += a[i][j] ^ b[i][j]
    return cnt


def main(n):
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

    board = []

    # Deterministic generation of 4 boards of size n x n
    # Board 0: all zeros
    b0 = [[0 for _ in range(n)] for _ in range(n)]
    board.append(b0)

    # Board 1: all ones
    b1 = [[1 for _ in range(n)] for _ in range(n)]
    board.append(b1)

    # Board 2: row-based pattern
    b2 = [[i % 2 for _ in range(n)] for i in range(n)]
    board.append(b2)

    # Board 3: column-based pattern
    b3 = [[j % 2 for j in range(n)] for _ in range(n)]
    board.append(b3)

    a_cnts = []
    b_cnts = []
    for b0 in board:
        heapq.heappush(a_cnts, doxor(b0, a))
        heapq.heappush(b_cnts, doxor(b0, b))

    result = (
        heapq.heappop(a_cnts)
        + heapq.heappop(a_cnts)
        + heapq.heappop(b_cnts)
        + heapq.heappop(b_cnts)
    )
    # print(result)
    pass
if __name__ == "__main__":
    main(5)
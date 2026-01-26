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

    # Deterministic generation of 4 boards of size n x n,
    # each entry is 0 or 1, derived from simple arithmetic on i, j and board index.
    boards = []
    for k in range(4):
        board_k = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append((i + j + k) % 2)
            board_k.append(row)
        boards.append(board_k)

    a_cnts = []
    b_cnts = []
    for b0 in boards:
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
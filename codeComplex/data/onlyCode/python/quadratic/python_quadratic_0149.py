import heapq


def doxor(a, b):
    cnt = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            cnt += a[i][j] ^ b[i][j]
    return cnt


n = int(input())

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
board.append([list(map(int, list(input()))) for _ in range(n)])
input()
board.append([list(map(int, list(input()))) for _ in range(n)])
input()
board.append([list(map(int, list(input()))) for _ in range(n)])
input()
board.append([list(map(int, list(input()))) for _ in range(n)])

a_cnts = []
b_cnts = []
for b0 in board:
    heapq.heappush(a_cnts, doxor(b0, a))
    heapq.heappush(b_cnts, doxor(b0, b))

print(heapq.heappop(a_cnts) + heapq.heappop(a_cnts) +
      heapq.heappop(b_cnts) + heapq.heappop(b_cnts))

# A. Find Square

n, m = map(int, input().split())

top = [-1, -1]
bottom = [-1, -1]

matrix = list()
for i in range(n):
    s = input()
    matrix.append(s)

for i in range(n):
    left = matrix[i].find('B')
    if left != -1:
        top[0] = i
        top[1] = left
        break

for i in range(n-1, -1, -1):
    right = matrix[i].rfind('B')
    if right != -1:
        bottom[0] = i
        bottom[1] = right
        break

print(1 + top[0] + (bottom[0] - top[0]) // 2, 1 + top[1] + (bottom[1] - top[1]) // 2)

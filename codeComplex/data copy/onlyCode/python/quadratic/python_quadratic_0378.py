# A. Find Square

n, m = map(int, input().split())

top = [-1, -1]
bottom = [-1, -1]

for i in range(n):
    s = input()
    left = s.find('B')
    if left != -1:
        right = s.rfind('B')
        c = (right - left) // 2 + 1
        print(i + c, left + c)
        break

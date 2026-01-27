n = int(input())

x, y = map(int, input().split())

ans = (x - 1) + (y - 1) <= (n - x) + (n - y)
print('White' if ans else 'Black')

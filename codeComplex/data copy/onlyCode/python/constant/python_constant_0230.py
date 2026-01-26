a, b = map(int, input().split())
x, y, z = map(int, input().split())
needa = 2 * x + y
needb = y + 3 * z
print(max(0, needa - a) + max(0, needb - b))
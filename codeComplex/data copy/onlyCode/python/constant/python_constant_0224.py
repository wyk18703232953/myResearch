yellow, blue = map(int, input().split())
y, g, b = map(int, input().split())

count = 0

yt = y * 2 + g
bt = g + b * 3

yc = yellow - yt
if yc < 0:
    count += abs(yc)

bc = blue - bt
if bc < 0:
    count += abs(bc)

print(count)





# while True:
#     if yellow > 0:
#         y = ny * 2
#         yellow -= y
#         yellow = yellow - g
#         break
#     else:
#         yellow += 1
#         count += 1
#         break
#
# while True:
#     if blue > 0:
#         blue = blue - g
#         nb = nb * 3
#         blue = blue - nb
#         break
#     else:
#         blue += 1
#         count += 1
#         break
#
# print(count)

yellow, blue = map(int, input().split())
x, y, z = map(int, input().split())
answer1 = x*2+y-yellow
answer2 = z*3+y - blue
if answer1 > 0:
    if answer2 > 0:
        print(answer1+answer2)
    else:
        print(answer1)
else:
    if answer2 > 0:
        print(answer2)
    else:
        print(0)

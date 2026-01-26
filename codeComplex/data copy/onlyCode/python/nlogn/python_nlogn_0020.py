# A. Second Order Statistics

n = int(input())
a = sorted(set(map(int, input().split())))

if len(a) > 1:
    x = iter(a)
    next(x)
    print(next(x))
else:
    print("NO")

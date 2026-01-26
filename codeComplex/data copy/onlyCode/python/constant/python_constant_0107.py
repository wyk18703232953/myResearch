def operations(a, b):
    less = min(a, b)
    more = max(a, b)
    ops = 0
    while less > 0 and more > 0:
        ops += more // less
        more -= less * (more // less)
        less, more = more, less
    return ops

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(operations(a, b))

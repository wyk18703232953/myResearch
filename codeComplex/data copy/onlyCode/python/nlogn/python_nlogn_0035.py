input()
a = sorted(list(map(int, input().split())))
print(*(*a[:-1], 2) if a[-1] == 1 else (1, *a[:-1]))
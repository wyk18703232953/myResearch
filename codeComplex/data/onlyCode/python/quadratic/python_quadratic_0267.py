n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
lst = []
for i in range(len(a)):
    if (a[i] in b):
        lst.append(a[i])
if (len(lst) == 0):
    pass
else:
    print(*lst)

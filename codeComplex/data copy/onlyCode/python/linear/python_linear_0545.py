n = int(input())
a = list(map(int, input().split()))
mx = -1
for step, elem in enumerate(a):
    if elem > mx + 1:
        print(step + 1)
        exit(0)
    else:
        mx = max(mx, elem)
print(-1)

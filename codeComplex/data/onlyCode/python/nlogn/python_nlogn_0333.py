lis = []
for _ in range(int(input())):
    lis.append(input())
lis = sorted(lis, key=len)

for i in range(len(lis) - 1):
    if(lis[i] not in lis[i + 1]):
        print("NO")
        exit(0)

print("YES")
for i in lis:
    print(i)

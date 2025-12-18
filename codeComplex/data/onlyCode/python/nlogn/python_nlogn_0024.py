n = int(input())
l = list(map(int,input().split()))



l = set(l)
l = list(l)


if len(l)<=1:
    print("NO")
    exit()
    
l.sort()
print(l[1])
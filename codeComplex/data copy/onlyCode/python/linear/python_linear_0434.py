n = int(input())

l = []
for i in range(n):
    c = list(map(int, input().split()))
    l.append(sum(c))

m = l[0]
l.sort(reverse=True)
for i in range(len(l)):
    if m == l[i]:
        print(i+1)
        break


    

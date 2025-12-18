n = int(input())

first = list(input())
second = list(input())

swap = list()
can = True

for i in range(n):
    if first[i] != second[i]:
        cont = -1
        for j in range(i,n): 
            if first[j] == second[i]:
                cont = j 
                break
            
        if cont != -1:
            for j in range(cont, i, -1 ):
                first[j], first[j-1] = first[j-1], first[j]
                swap.append(j)
        else:
            can = False

if can: 
    print(len(swap))
    print(*swap, end=' ')

else: 
    print(-1)
n=int(input())
S=[]
for i in range(n):
    A=[int(i) for i in input().split()]
    S.append(sum(A))
if S[0]==max(S):
    print("1")
    exit()
thomas=S[0]
rank=1
S.sort(reverse=True)
for i in S:
    if i == thomas:
        print(rank)
        exit()
    else:
        rank+=1            
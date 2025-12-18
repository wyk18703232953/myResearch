from collections import deque
n=int(input())
orderedli=list(map(int,input().split(" ")))


indexof={}
for i,x in enumerate(orderedli):
    indexof[x]=i+1

sortedli=list(sorted(orderedli))
i=0

s=input()

st=deque()

for x in s:
    if x=="0":
        st.append(sortedli[i])
        print(indexof[sortedli[i]],end=" ")
        i += 1
    else:#x==1
        temp=st.pop()
        print(indexof[temp],end=" ")

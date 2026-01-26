n=int(input())
w = [(int(x), c+1) for c, x in enumerate(input().split())]
b=sorted(w,reverse=True)    
f=[]
p=[]
k=input()
for i in k:
    if i=="0":
        x=b.pop()
        f.append(x)
        p.append(x[1])
    else:
        y=f.pop()
        p.append(y[1])
print(*p) 
  	 	 	 					   	 		 		 			 			
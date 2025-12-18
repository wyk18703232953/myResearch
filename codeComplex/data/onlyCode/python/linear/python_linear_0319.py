n=int(input())
a=b=[]
k=0
for _ in range(n): 
	a.append(input())
for i in range(n):
	t=input()
	if t in a:
		a.remove(t)
print(len(a))
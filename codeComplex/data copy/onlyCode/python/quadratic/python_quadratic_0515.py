n,m=map(int,raw_input().split())

l=[]
for i in range(n):
	s=raw_input()
	l.append([])
	for j in range(m):
		l[-1].append(s[j])

ans=[]
for i in range(n):

	ans.append([])
	for j in range(m):
		ans[-1].append(".")

for i in range(n-2):
	for j in range(m-2):
		if l[i][j]=="#":
			if l[i][j]==l[i][j+1] and l[i][j]==l[i][j+2] and l[i][j]==l[i+1][j] and l[i][j]==l[i+1][j+2] and l[i][j]==l[i+2][j] and l[i][j]==l[i+2][j+1] and l[i][j]==l[i+2][j+2]:
				ans[i][j]="#"
				ans[i][j+1]="#"
				ans[i][j+2]="#"
				ans[i+1][j]="#"
				ans[i+1][j+2]="#"
				ans[i+2][j]="#"
				ans[i+2][j+1]="#"
				ans[i+2][j+2]="#"

flag = True
for i in range(n):
	for j in range(m):
		if l[i][j]!=ans[i][j]:
			flag = False
			break
	if flag==False:
		break

if flag==True:
	print("YES")
else:
	print("NO")


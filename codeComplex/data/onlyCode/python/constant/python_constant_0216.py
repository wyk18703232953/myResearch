l=list(map(int,input().split()))
s1,s2,s3,s4=0,0,0,0
for i in l:
	if i==1:
		s1+=1
	if i==2:
		s2+=1
	if i==3:
		s3+=1
	if i==4:
		s4+=1
# print(s1,s2,s3)
if s3>2 or s2>1 or s1>0 or (s4==2 and s2==1):
	print("YES")
else:
	print("NO")
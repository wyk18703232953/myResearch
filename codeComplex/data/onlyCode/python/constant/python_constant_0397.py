s=[list(input()) for i in range(2)]
n=len(s[0])
cnt=0
for i in range(n-1):
  if s[0][i]==s[1][i]==s[0][i+1]=="0":
    cnt+=1
    s[0][i]=s[1][i]=s[0][i+1]="X"
  elif s[0][i]==s[1][i]==s[1][i+1]=="0":
    cnt+=1
    s[0][i]=s[1][i]=s[1][i+1]="X"
  elif s[0][i]==s[1][i+1]==s[0][i+1]=="0":
    cnt+=1
    s[0][i]=s[1][i+1]=s[0][i+1]="X"
  elif s[0][i+1]==s[1][i]==s[1][i+1]=="0":
    cnt+=1
    s[0][i+1]=s[1][i]=s[1][i+1]="X"
print(cnt)
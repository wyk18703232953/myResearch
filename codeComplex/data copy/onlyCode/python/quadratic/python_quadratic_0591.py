
import sys
input = sys.stdin.readline
q=int(input())
for i in range(q):
  n,k=map(int,input().split())
  s=input()
  a=k
  for j in range(n-k+1):
    a1,a2,a3=0,0,0
    for jj in range(k):
      if jj%3==0:
        if s[j+jj]=="R":
          a2+=1
          a3+=1
        elif s[j+jj]=="G":
          a1+=1
          a3+=1
        else:
          a1+=1
          a2+=1
      elif jj%3==1:
        if s[j+jj]=="R":
          a1+=1
          a2+=1
        elif s[j+jj]=="G":
          a2+=1
          a3+=1
        else:
          a3+=1
          a1+=1
      else:
        if s[j+jj]=="R":
          a1+=1
          a3+=1
        elif s[j+jj]=="G":
          a1+=1
          a2+=1
        else:
          a3+=1
          a2+=1
    a=min(a,a1,a2,a3)
  print(a)
      



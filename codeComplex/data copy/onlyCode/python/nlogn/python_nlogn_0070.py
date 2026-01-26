t=int(input())
l=list(map(int,input().split()))
b_sum=0
l.sort()
for i in l:
  b_sum += i

m_sum=0
c=0
for i in l[::-1]:
  m_sum += i
  c += 1
  if m_sum > (b_sum/2):
    break
print(c)
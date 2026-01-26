
def val(s):
  ans = ((int(s.split('+')[0][1:]) + int(s.split('+')[1].split(')')[0])) / int(s.split('/')[1]))
  return ans 

n = int(input())
s = []
f = {}
for i in range(n):
  ss = input()
  s.append(val(ss))
  if(s[i] not in f):
    f[s[i]] = 1 
  else:
    f[s[i]] += 1

for i in range(len(s)):
  print(f[s[i]], end= " ")
print()


s1=input()
s2=input()
arr=list(s1)
arr.sort(reverse=True)
if(len(s2)>len(s1)):
  t=""
  for i in arr:
    t+=i
  print(t)
else:
  t=""
  l =len(s1)
  for i in range(l):
    index=-1
    ma = -1
    for j in range(len(arr)):
      temp = arr[j]
      tt=[]
      for k in range(len(arr)):
        if(k!=j):
          tt.append(arr[k])
      tt.sort()
      for k in tt:
        temp+=k
      temp = t+temp
      # print(temp,"fhhh")
      if(int(s2)>=int(temp)):
        # print(temp,"f")
        if(int(arr[j])>ma):
          ma = int(arr[j])
          index = j
    t+=arr[index]
    del arr[index]
    # print(t,arr)
  print(t)




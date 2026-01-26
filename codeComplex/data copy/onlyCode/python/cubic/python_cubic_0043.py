a = input()
l = 0
for i in range(1, len(a)):
  for j in range(0, len(a) - i + 1):
    #print(a[j:j + i + 1], i, j)
    t = a.find(a[j:j + i])
    c = a.rfind(a[j:j + i])
    #print(t, c)
    if t != c:
      if i > l:
        l = i
print(l)
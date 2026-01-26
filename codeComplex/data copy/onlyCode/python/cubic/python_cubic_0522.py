def permuteDigits(a, b):
    
    n = len(a)
    if len(a) < len(b):
        return a
        
    i = 0
    c = 0
    t = a[0]
    flag = 0
    lastind = []
    while i<len(a) and i< len(b) and a[i] >= b[i] :
#        print("i:",i,"c:",c,"  a:",a,"  b:",b)
        
        if c == n:
            i = i - 1
            t = a[i]
            a = a[:i] + a[i+1:]
            a.insert(lastind.pop(),t)
            flag = 1
            c = i
        elif (flag == 0 and a[c] == b[i]) or a[c] < b[i]:        
            lastind.append(c)
            t = a[c]            
            a = a[:c] + a[c+1:]
#            print("i:",i,"  a:",a,"  b:",b,"  t:",t,"  c:",c,"  li:",lastind)
            a.insert(i,t)
#            print("i:",i,"  a:",a,"  b:",b,"  t:",t,"  c:",c,"  li:",lastind)        
        else:
            c = c + 1

        if a[i] < b[i]:
            break
        elif flag == 0 and a[i] == b[i]:
            i = i + 1                
            c = i            
#        print("i:",i,"  a:",a,"  b:",b,"  t:",t,"  c:",c)            
    return a

#     98175987
# Ans 98598771
#     98598771
# Lim 98715689
    
aa = input()
bb = input()

a=[]
b=[]
for i in aa:
    a.append(int(i))
for i in bb:
    b.append(int(i))

a.sort(reverse=True)

ans = permuteDigits(a, b)
s = ""
for i in ans:
    s = s + str(i)
print(int(s))
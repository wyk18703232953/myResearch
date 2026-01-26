a = list(input())
b = list(input())
n = len(a)
a.sort()

def listtostring(string):
    return ''.join([str(ele) for ele in string])


for i in range(0,n):
    for j in range(0,n):
        t = a.copy()
        t[i],t[j] = t[j],t[i]
        if((int(listtostring(t)) >= int(listtostring(a))) and (int(listtostring(t))<= int(listtostring(b)))):
         #   print("BEFORE",a,a[i],a[j],i,j)
            a[i],a[j] = a[j],a[i]
         #   print("AFTER",a,a[i],a[j],i,j)
        
print(listtostring(a))
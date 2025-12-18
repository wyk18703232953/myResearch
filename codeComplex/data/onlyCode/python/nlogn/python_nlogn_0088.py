n , k = map(int , input().split())
lst = []
for i in range(n):
    p , t =  map(int , input().split())
    lst.append([p,-t])
    
tmp  = sorted(lst , key =lambda x : (x[0],x[-1]) , reverse = True)[k-1]
print(lst.count(tmp))
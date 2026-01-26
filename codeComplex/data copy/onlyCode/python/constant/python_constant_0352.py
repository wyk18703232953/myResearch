n=int(input())
d={"purple":"Power","green":"Time","blue":"Space","orange":"Soul","red":"Reality","yellow":"Mind"}
l=[]
for i in range(n):
    s=input()
    l.append(s)
print(6-n)
for i in d:
    if i not in l:
        print(d[i])
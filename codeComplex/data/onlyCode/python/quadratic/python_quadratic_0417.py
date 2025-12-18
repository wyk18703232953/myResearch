tam,q = [int(i) for i in input().split()]
t = input()
s = t

posi = -1

for j in range(tam-1):
    if(t[:j+1] == t[tam - j -1:]):
        posi = j

add = t[posi+1:]

for j in range(q-1):
    s += add
    
print(s)
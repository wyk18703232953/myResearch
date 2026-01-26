a=int(input())
l=[]
total=0
for i in range(4):
    line=''

    for x in [0]*a:
        line+=input()    
    l.append(line)
    input() if i!=3 else 0
l=sorted(l,key=lambda i: i[0::2].count('1')+i[1::2].count('0'))[::-1]
for z,v in enumerate(l):
    if z<2:
        for i in range(a**2):
            total += v[i]!='0' if i%2 else v[i]!='1'
    else:
        for i in range(a**2):
            total += v[i]!='1' if i%2 else v[i]!='0'
print(total)
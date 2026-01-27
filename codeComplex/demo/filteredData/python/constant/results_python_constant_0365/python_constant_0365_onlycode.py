allcolor=['purple','green','blue','orange','red','yellow']
op=['Power', 'Time', 'Space', 'Soul', 'Reality', 'Mind']
n=int(input())
ipcolor=[]
for i in range(0,n):
    color=input()
    ipcolor.append(color)
diff=list(set(allcolor) - set(ipcolor))
print(len(diff))
for i in range(0,len(diff)):
    print(op[allcolor.index(diff[i])])
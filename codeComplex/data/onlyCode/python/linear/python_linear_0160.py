f=input
D,E=dict(),[eval(f())for i in range(int(f()))]
for e in E:D[e]=D.get(e,0)+1
for e in E:print(D[e])
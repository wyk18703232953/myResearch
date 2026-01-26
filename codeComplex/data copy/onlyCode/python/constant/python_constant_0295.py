from math import *
k,n,s,p = map(int,input().split())
sheetsforone = ceil(n/s)
sheetsfork = sheetsforone*k
packs = ceil(sheetsfork/p)
print(int(packs))
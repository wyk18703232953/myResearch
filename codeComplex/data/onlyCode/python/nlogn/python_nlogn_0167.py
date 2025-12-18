import io
import os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


n = int(input())

endpoints = []

for x in range(n):
    p, w = map(int, input().split())
    endpoints.append([p-w, p+w])

#bruh
endpoints.sort(key=lambda sublist: sublist[1])

res = 0

#print(endpoints)

bottom = 10**18 * -1

for pt in range(len(endpoints)):
    if endpoints[pt][0] >= bottom:
        res += 1
        bottom = endpoints[pt][1]

print(res)



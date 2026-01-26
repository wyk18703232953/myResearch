n, m = map(int, input().split())
daf1 = list(map(int, input().split()))
daf2 = dict()

for i in range(n):
    daf2[i+1] = 0

for i in daf1:
    if i in daf2.keys():
        daf2[i] += 1

print(min(daf2.values()))

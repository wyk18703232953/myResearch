__author__ = 'ruckus'

n = int(input())
s = input()
t = input()
dif = {}
hem = 0
for i in range(n):
    if s[i] != t[i]:
        dif[i] = [s[i], t[i]]
        hem += 1

change = []
probed = []
k = 0
for i in dif.keys():
    if dif[i] in probed:
        continue
    probed.append(dif[i])
    k += 1
    for j in list(dif.keys())[k:]:
        if dif[i] == dif[j][::-1]:
            print(hem - 2)
            print(i + 1, j + 1)
            quit()
        if not change and (dif[i][0] == dif[j][1] or dif[j][0] == dif[i][1]):
            change = [i, j]

if change:
    print(hem - 1)
    print(change[0] + 1, change[1] + 1)
else:
    print(hem)
    print('-1 -1')
n = int(input())
a = list(map(int, input().split()))
chet = 0
ne_chet = 0
chet1 = []
ne_chet1 = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        chet += 1
        chet1.append(a[i])
    else:
        ne_chet += 1
        ne_chet1.append(a[i])
    if chet >= 1 and ne_chet >= 1 and (chet > 1 or ne_chet > 1):
        break
if chet == 1:
    print(a.index(chet1[0]) + 1)
elif ne_chet == 1:
    print(a.index(ne_chet1[0]) + 1)

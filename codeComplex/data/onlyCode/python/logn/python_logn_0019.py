l, r = map(int, input().split())

if l == r:
    print(0)
    exit()
binr, binl = list(bin(r)[2:]), list(bin(l)[2:])
binl = ['0'] * (len(binr) - len(binl)) + binl
# print(binl, binr)
for i in range(len(binl)):
    if binl[i] != binr[i]:
        binl = '1' * (len(binl[i:]))
        break

print(int(binl, 2))
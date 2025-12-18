a, b = map(int, input().split())
if a == b:
    print(0)
    exit()
aa = ""
bb = ""
while a or b:
    aa += str(a % 2)
    bb += str(b % 2)
    a //= 2
    b //= 2
aa = aa[::-1]
bb = bb[::-1]
# print(aa)
# print(bb)
idx = 0
while aa[idx] == bb[idx]:
    idx += 1
# print(idx)
ln = len(aa)
r = 2 ** (ln - idx) - 1
print(r)

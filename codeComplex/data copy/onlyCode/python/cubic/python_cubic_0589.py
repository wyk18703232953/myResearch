import sys

a, b = input(), input()

if len(a) < len(b):
    print(*sorted(a, reverse=True), sep='')
    exit()

cnt = [0]*10

for x in a:
    cnt[int(x)] += 1


def rec(res, digit, rem):
    if digit == len(b):
        return res
    if rem[int(b[digit])]:
        r = rem[:]
        r[int(b[digit])] -= 1
        x = rec(res + b[digit], digit+1, r)
        if x:
            return x
    for d in range(int(b[digit])-1, -1, -1):
        if rem[d]:
            res += str(d)
            rem[d] -= 1
            suf = []
            for i in range(10):
                suf += [str(i)] * rem[i]
            return res + ''.join(sorted(suf, reverse=True))
    return ''


ans = rec('', 0, cnt[:])
print(ans)

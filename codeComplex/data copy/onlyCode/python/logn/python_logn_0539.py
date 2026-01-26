n = int(input())
maxlength = 12

lengths = [1]
for i in range(1, maxlength+1):
    lengths.append(lengths[i-1]+9*i*(10**(i-1)))


def getnum(n):
    global lengths
    mx = maxlength - 1
    mn = 0
    while 1:
        chk = (mx - mn) // 2
        if chk == 0:
            break
        chk += mn
        if n < lengths[chk]:
            mx = chk
        else:
            mn = chk
    curlength = mx
    curlength_ind = n - lengths[curlength - 1]
    curdigind = curlength_ind % curlength
    beforenumscount = curlength_ind // curlength
    result = 0 + (beforenumscount // (10 ** (curlength - curdigind - 1)) + (curdigind == 0)) % 10
    return result

print(getnum(n))




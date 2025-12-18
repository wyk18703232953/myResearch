success = 0
def solve(b, freq, i, n, res):
    global success
    if i == len(b):
        success = res
    else:
        success = 0
        move = 9
        while move >= 0 and success == 0:
            m = int(b[i])
            if freq[move] > 0 and res * 10 + move <= n * 10 + m:
                res = res * 10 + move
                n = n * 10 + m
                freq[move] -= 1
                if solve(b, freq, i + 1, n, res) == 0:
                    res //= 10
                    n //= 10
                    freq[move] += 1
            move -= 1
    return success

a = input()
b = input()
freq = []
for i in range(10):
    freq.append(0)
v = []
for x in a:
    n = int(x)
    v.append(n)
    freq[n] += 1
v.sort()
ans = 0
if len(b) > len(a):
    m = 1
    for x in v:
        ans = x * m + ans
        m *= 10
else:
    ans = solve(b, freq, 0, 0, 0)
print(ans)
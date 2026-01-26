import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
x.sort()
s = set(x)
m, ans = 1, [x[0]]
pow2 = [1]
for _ in range(35):
    pow2.append(2 * pow2[-1])
for i in x:
    for j in pow2:
        if (i - j) in s and (i + j) in s:
            m = 3
            ans = [i - j, i, i + j]
            break
        elif (i - j) in s and m < 2:
            m = 2
            ans = [i, i - j]
        elif (i + j) in s and m < 2:
            m = 2
            ans = [i, i + j]
    if m == 3:
        break
print(m)
print(*ans)
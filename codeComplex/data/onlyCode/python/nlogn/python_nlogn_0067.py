n = int(input())
a = list(map(int, input().split()))
b = sorted(a,reverse=True)
total = sum(a)
gain = 0
num = 0
for x in range(len(b)):
    gain += b[x]
    num += 1
    if gain>total/2:
        break
print(num)
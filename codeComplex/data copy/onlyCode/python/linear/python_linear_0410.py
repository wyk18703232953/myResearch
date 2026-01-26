a, b = map(int, input().split())
c = input()
sorted(c)
summa = 0
count = 0
j = -2
i = 0
abc = "abcdefghijklmnopqrstuvwxyz"
while i < 26 and count < b:
    if abc[i] in c and i-2 >= j:
        summa += i+1
        count += 1
        j = i
    i += 1
if count < b:
    print(-1)
else:
    print(summa)
n = int(input())
a = input()
sum = 0
for x in a:
    sum += int(x)
ans = "NO"
if sum == 0:
    ans = "YES"
s = 1
while s * s <= sum and ans == "NO":
    if sum % s == 0:
        t = 0
        flag = 0
        for x in a:
            t += int(x)
            if t == s:
                flag = 1
            if t > s:
                if flag == 1:
                    flag = 0
                    t = int(x)
                    if t == s:
                        flag = 1
        if t == s and t != sum:
            ans = "YES"
        t = 0
        flag = 0
        for x in a:
            t += int(x)
            if t == sum // s:
                flag = 1
            if t > sum // s:
                if flag == 1:
                    flag = 0
                    t = int(x)
                    if t == sum // s:
                        flag = 1
        if t == sum // s and t != sum:
            ans = "YES"  
    s += 1
print(ans)
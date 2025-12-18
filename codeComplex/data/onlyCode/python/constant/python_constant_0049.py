n = int(input())
k = set("47")
p = False
for i in range(1, n+1):
    if n%i == 0:
        if set(str(i)) <= k:
            p = bool(set(str(i)))
            break       
if p == True:
    print("YES")
else:
    print("NO") 
n = int(input())
x  = input()
l = list(map(int, x.split()))
# print(n,l)
dict = {}
# print(type(dict))
for i in l:
    dict[i] = 0;
sum = 0
fre = 0
ans = 0
for i in range(n-1,-1, -1):
    # print(i)
    x = sum
    y = fre
    for j in range(-1,2):
        aa = l[i]+j
        if aa in dict:
            x-= aa*dict[aa]
            y-= dict[aa]
        # print(x, y, l[i])
    ans += x - l[i]*y
    fre+=1
    sum+=l[i]
    dict[l[i]]+=1
print(ans)
# dict[2] = 3
# print(dict[4])
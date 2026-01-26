n = int(input())
s = input()
 
for sum in range(9 * n + 1):
    cnt = 0
    cursum = 0
    for i in s:
        cursum += int(i)
        if cursum == sum:
            cnt += 1
            cursum = 0
 
    if cursum == 0 and cnt > 1:
        print("YES")
        exit(0)
 
print("NO")
k = int(input())
n = 1
up_bnd = 9
while(k > up_bnd):
    n += 1
    up_bnd += (9*n)*(10**(n-1))
low_bnd = 0
for i in range(1, n):
    low_bnd += (9*i)*(10**(i-1))
num = int((k-low_bnd)/n)
lb_val = 0
for i in range(n-1):
    lb_val = (lb_val*10)+9
num += lb_val
rm = (k-low_bnd) % n
if(rm != 0):
    num += 1
ans = 0
if(rm == 0):
    ans = num % 10
else:
    for i in range(n-rm+1):
        j = (num % 10)
        num = int(num/10)
        ans = j
print(int(ans))

idx = {}
idx[0] = 0
s = 0
num = 9
for digit in range(1,12):
    s += num*digit
    #print(s)
    idx[digit] = s
    num = num*10
    
N = int(input())

nubmer = 0
r = 0
d = 0
for digit in range(1,12):
    if N<=idx[digit] and N>idx[digit-1]:
        #print(digit)
        number = (N-idx[digit-1])//digit
        r = (N-idx[digit-1])%digit
        d = digit
        break
    
if r!=0:
    number += 1

num = 10**(d-1) + number - 1
#print(num,r)
# if r==0, last digit
digit = [int(i) for i in str(num)]
if r==0:
    print(digit[-1])
# if r!=0, search digit from left to right
else:
    print(digit[r-1])
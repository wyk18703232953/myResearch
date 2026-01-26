# -*- coding: utf-8 -*-

n = int(input())

lucky = ["1","2","3","5","6","8","9","0"]


ye = False
for i in range(1,n+1):
    luck=True
    for char in str(i):
        if char in lucky:
            luck = False
            break
            
    if luck == True and n % i == 0:
        print("YES")
        ye = True
        break
    else:
        continue
if ye != True:
    print("NO")
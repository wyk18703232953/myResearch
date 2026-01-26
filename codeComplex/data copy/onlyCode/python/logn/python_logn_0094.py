import sys

SIZE = 105
a = SIZE * [0]
b = SIZE * [0]


lr = input().split()
l = int(lr.pop(0))
r = int(lr.pop(0))

if l == r:
    print(0)

else:
    len1 = 0
    len2 = 0
    while l != 0:
        a[len1] = l % 2
        l = int(l/2)
        len1 += 1

    while r != 0:
        b[len2] = r % 2
        r = int(r/2)
        len2 += 1

    tag = 0
    for i in range(max(len1, len2)-1, 0, -1):
        if b[i] == 1 and a[i] == 0:
            tag = i
            break

    print(pow(2, tag+1)-1)

    				   		 	 					 		 	 			
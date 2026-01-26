n, m = map(int, input().split())
a = input()
b = input()
flag = 0
for c in a:
    if(c == '*'):
        flag = 1
if(flag == 1):
    a1, a2 = a.split('*')
    Len1 = len(a1)
    Len2 = len(a2)
    b1 = b[:Len1]
    b2 = ''
    if(Len2):
        b2 = b[-Len2:]
    #print(a1, b1, a2, b2)
    if(a1 == b1 and a2 == b2 and Len1 + Len2 <= len(b)):
        print('YES')
    else:
        print('NO')
else:
    if(a == b):
        print('YES')
    else:
        print('NO')

   	 	   	 			 		 	 			 	  		 	
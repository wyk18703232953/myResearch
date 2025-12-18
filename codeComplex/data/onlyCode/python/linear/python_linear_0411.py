a, b = map(int, input().split())
c = input()
su = 0
cnt = 0
j = -2
i = 0
lis = "abcdefghijklmnopqrstuvwxyz"
while i < 26 and cnt < b:
    if lis[i] in c and i-2 >= j:
        su += i+1
        cnt += 1
        j = i
    i += 1
if cnt < b:
    print(-1)
else:
    print(su)
    	  			 		 	 		 	 			 			
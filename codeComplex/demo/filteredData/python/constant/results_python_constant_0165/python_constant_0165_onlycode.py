l,r=map(int,input().split())
j=r-l+1

# basically two even numbers can never be coprime so we will check can we have three numbers 
# such that we can have 2 even and 1 odd 

# if gap consists number less than 3 then output would be -1
# if gap is of 3 it must start with even like 2-4 we have 2 3 4
# if it starts with 5-7 we can write 5 6 7 
if j==3:
	if l%2==0:
		print(l,l+1,l+2)
	else:
		print(-1)
elif j>3:
	if l%2==0:print(l,l+1,l+2)
	else:print(l+1,l+2,l+3)
else:print(-1)
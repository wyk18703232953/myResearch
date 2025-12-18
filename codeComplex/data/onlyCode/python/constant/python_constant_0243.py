
n=int(input())
m=int(input())
# x=(2**n)
if n>(m+1)/2:
	print(m)
else:
	print(int(m%(2**n)))
# print(x)
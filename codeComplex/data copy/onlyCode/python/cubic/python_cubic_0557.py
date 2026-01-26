a=sorted(input())

b=int(input())

a=a[::-1]

p=""

while a:

	for i, z in enumerate(a):

		n=p+a[i]+"".join(sorted(a[:i]+a[i+1:]))

		if int(n)<=b:

			p+=z

			a.pop(i)

			break

print(p)



# Made By Mostafa_Khaled
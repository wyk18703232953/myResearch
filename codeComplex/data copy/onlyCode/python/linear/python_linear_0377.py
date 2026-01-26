a=input()
c1=a.count('1')
a=a.split('2')
lex='0'*a[0].count('0')+'1'*c1
n=len(a)
for i in range(1,n):
  lex=lex+'2'+'0'*a[i].count('0')
print(lex)
     			 	 	       	 	 	 	   	
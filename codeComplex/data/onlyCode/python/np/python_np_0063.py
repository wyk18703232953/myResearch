list1=list(input())
list2=list(input())
plus1=list1.count('+')
plus2=list2.count('+')
minus1=list1.count('-')
minus2=list2.count('-')
wths=list2.count('?')
def giveFactorial(n,x):
    if x==0 or x==n or x>n or n==0:
        return 1
    else:
        return giveFactorial(n-1,x-1)+giveFactorial(n-1,x)
a=(giveFactorial(wths,plus1-plus2))
#print(wths,plus1-plus2)
if plus1==plus2 and wths==0:
    print(1)
elif wths==0 :
    print(0)
elif plus1-plus2>wths or minus1-minus2>wths:
    print(0)
else:
    print((0.5**(plus1-plus2+minus1-minus2))*a)
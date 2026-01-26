from math import factorial


def C(k, n):
    return factorial(n) // factorial(k) // factorial(n - k)


s1 = input()
s2 = input()
n1 = s1.count('+')
n2 = s2.count('+')
n3 = s2.count('?')
if n2 > n1:
    print(0)
else:
    try:
        print(C(n1 - n2, n3) / (2 ** n3))
    except:
        print(0)

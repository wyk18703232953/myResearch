from math import factorial as fact

a = input()
b = input()

aplus = a.count('+')
aminus = len(a) - aplus

bplus = b.count('+')
bminus = b.count('-')
bjolly = len(b) - bplus - bminus

if bplus > aplus or bminus > aminus:
    print(0)
else:
    c = aplus-bplus
    res = fact(bjolly) / fact(bjolly-c) / fact(c) / 2**bjolly
    print(res)

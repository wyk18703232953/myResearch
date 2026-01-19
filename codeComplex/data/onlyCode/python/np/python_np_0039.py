from math import factorial
drazil = input()
dreamoon = input()
net_drazil = 0
net_dreamoon = 0
uncretain_count = 0
for i in drazil:
    if i == '-':
        net_drazil -= 1
    else:
        net_drazil += 1
for i in dreamoon:
    if i == '-':
        net_dreamoon -= 1
    elif i == '+':
        net_dreamoon += 1
    else:
        uncretain_count += 1
x = (uncretain_count + (net_drazil - net_dreamoon)) // 2
y = (uncretain_count - (net_drazil - net_dreamoon)) // 2
#print(x,y)
if abs(x) + abs(y) != uncretain_count:
    print(0.0)
else:
    out = factorial(uncretain_count)//(factorial(x)*factorial(uncretain_count-x))
    print(out/2**uncretain_count)


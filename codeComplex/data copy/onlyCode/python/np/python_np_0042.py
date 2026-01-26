import math
a = str(input())
b = str(input())
posa = a.count('+') - a.count('-')
posb = b.count('+') - b.count('-')
q = b.count('?')
dist = (posa - posb)
ones = (abs(dist) + q) / 2
if q < abs(dist) or ((dist+q) % 2):
    ans = 0
else:
    ans = float(math.factorial(q)/(math.factorial(ones)*math.factorial(q-ones)))
    ans /= pow(2, q)
print(f'{ans:.9f}')

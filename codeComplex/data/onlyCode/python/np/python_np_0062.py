import math
s = input()
s1 = input()
plus=s.count('+')-s1.count('+')
minus=s.count('-')-s1.count('-')
v = s1.count('?')
if plus<0 or minus<0:
    print(0)
    exit()
print((math.factorial(v)/math.factorial(v-plus)/math.factorial(plus))*(0.5**v))
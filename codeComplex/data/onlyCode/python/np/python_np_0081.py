from collections import Counter
import math

i1 = list(input())
i2 = list(input())

a = Counter(i1)
b = Counter(i2)

c = b-a #Rem from b
d = a-b #Rem from a

c1 = list(c.elements())
d1 = list(d.elements())

count = 0
for i in c1:
  if i == "?":
    count = count+1   
if count != len(d1):
  print(0)
else:
  x = len(c1)
  that = 0
  for i in d1:
    if i == "+":
      that = that + 1
  out = math.factorial(x)/((math.factorial(that))*math.factorial(x-that))
  print(out/math.pow(2,x))




	   		     	   	   			 	  				
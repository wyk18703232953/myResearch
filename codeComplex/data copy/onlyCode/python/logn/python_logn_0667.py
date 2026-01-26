import math

n, k = input().split(" ")

n = int(n)
k = int(k)

variableone = 2 * (n + k) #the right side of the equation

# a = 1  b = 3  c = variableone

# x^2 +3x - 2(n+k)

# (-b + squareroot b^2 -4ac) / 2a

variabletwo = (-3 + math.sqrt(9 - 4 * 1 * (-1 * variableone))) / 2

variabletwo = int(variabletwo)

y = n - variabletwo

print(y)


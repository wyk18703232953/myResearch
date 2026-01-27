A,B = map(int, input().split())
x,y,z = map(int, input().split())
A1 = 2*x + y - A
B1 = 3*z + y - B
final = 0
if A1 > 0:
    final = final + A1
if B1 > 0:
    final = final + B1
print(final)
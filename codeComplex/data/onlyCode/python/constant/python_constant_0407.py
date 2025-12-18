x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
X1, Y1, X2, Y2, X3, Y3, X4, Y4 = map(int, input().split())

x = [x1, x2, x3, x4]
y = [y1, y2, y3, y4]
x = list(set(x))
y = list(set(y))
x.sort()
y.sort()
xl, xr = x
yl, yr = y

if xl <= X1 <= xr and yl  <= Y1 <= yr:
    print('YES')
    exit()
if xl <= X2 <= xr and yl  <= Y2 <= yr:
    print('YES')
    exit()
if xl <= X3 <= xr and yl  <= Y3 <= yr:
    print('YES')
    exit()
if xl <= X4 <= xr and yl  <= Y4 <= yr:
    print('YES')
    exit()

CX, CY = (X1+X2+X3+X4)//4,  (Y1+Y2+Y3+Y4)//4
X1, X2, X3, X4 = X1-CX, X2-CX, X3-CX, X4-CX
Y1, Y2, Y3, Y4 = Y1-CY, Y2-CY, Y3-CY, Y4-CY

if xl <= CX <= xr and yl  <= CY <= yr:
    print('YES')
    exit()

A = 0
for X in (X1, X2, X3, X4):
    A = max(A, abs(X))
if abs(x1-CX)+abs(y1-CY) <= A:
    print('YES')
    exit()
if abs(x2-CX)+abs(y2-CY) <= A:
    print('YES')
    exit()
if abs(x3-CX)+abs(y3-CY) <= A:
    print('YES')
    exit()
if abs(x4-CX)+abs(y4-CY) <= A:
    print('YES')
    exit()
print('NO')

import sys
input = sys.stdin.readline
x,y = map(int, input().split())
if y-x<2:
	print(-1)
elif x%2 != 0 and y-x==2:
	print(-1)
elif x%2==0:
	print(x, x+1, x+2)
else:
	print(x+1, x+2, x+3)
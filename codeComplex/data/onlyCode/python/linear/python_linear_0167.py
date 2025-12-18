import sys
input = sys.stdin.readline
n = int(input())
if n < 6:
    print(-1)

else:
    l = []
    o = []
    x = (3+n)//2
    for i in range(3,x+1):
        l.append((1,i))

    for i in range(x+1,n+1):
        o.append((2,i))

    sys.stdout.write("1"+" "+"2"+"\n")
    for x in l:
        sys.stdout.write(str(x[0]) + " " + str(x[1]) + "\n")

    for x in o:
        sys.stdout.write(str(x[0]) + " " + str(x[1]) + "\n")

sys.stdout.write("1"+" "+"2"+"\n")
p = 2
for i in range(3,n+1):
    sys.stdout.write(str(p) + " " + str(i) + "\n")
    p = i


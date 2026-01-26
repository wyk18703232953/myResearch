import sys, math

def mp():
    return list(map(int, input().split()))

def quer(x1, y1, x2, y2):
    if x1 > x2 or y1 > y2:
        return [0, 0]
    s = (x2 - (x1 - 1)) * (y2 - (y1 - 1))
    if s % 2 == 0:
        return [s // 2, s // 2]
    if (x1 + y1) & 1:
        return [s // 2 + 1, s // 2]
    return [s // 2, s // 2 + 1]
        

def main():
    q = int(input())
    for i in range(q):
        n, m = mp()
        x1, y1, x2, y2 = mp()
        s = quer(1, 1, n, m)
        s1 = quer(x1, y1, x2, y2)
        s[0] -= s1[0]
        s[1] += s1[0]
        
        # print(s[::-1])
        x3, y3, x4, y4 = mp()
        xmn = max(x1, x3)
        xmx = min(x2, x4)
        ymn = max(y1, y3)
        ymx = min(y2, y4)
        s1 = quer(x3, y3, x4, y4)
        s[0] += s1[1]
        s[1] -= s1[1]
        s1 = quer(xmn, ymn, xmx, ymx)
        s[0] += s1[0]
        s[1] -= s1[0]
        print(*s[::-1])
        
debug = 0
if debug:
    file = open("input.txt", "r")
    input = file.readline
main()
if debug:
    file.close()
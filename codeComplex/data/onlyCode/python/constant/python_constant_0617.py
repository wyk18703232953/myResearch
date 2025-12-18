import sys, math

def mp():
    return list(map(int, input().split()))

def ss(x):
    return x * (x + 1) // 2

def sol(x):
    if x == 0:
        return 0
    res = ss(x // 2) * 2
    res1 = ss(x) - res
    return res - res1

def main():
    q = int(input())
    for i in range(q):
        l, r = mp()
        print(sol(r) - sol(l - 1))
        
    
debug = 0
if debug:
    file = open("input.txt", "r")
    input = file.readline
main()
if debug:
    file.close()

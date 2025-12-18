import sys, math

def mp():
    return list(map(int, input().split()))

def main():
    n, k = mp()
    a = [2, 5, 8]
    s = 0
    for i in a:
        s += (n * i - 1) // k + 1
    print(s)
    
debug = 0
if debug:
    file = open("input.txt", "r")
    input = file.readline
main()
if debug:
    file.close()
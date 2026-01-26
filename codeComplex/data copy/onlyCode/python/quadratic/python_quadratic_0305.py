#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    r = 0
    while a:
        c = a[0]
        del a[0]
        for i in range(len(a)):
            if c == a[i]:
                break
        del a[i]
        r += i
    print(r)

if __name__ == "__main__":
    main()

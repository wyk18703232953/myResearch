from sys import stdin, gettrace

if gettrace():
    def inputi():
        return input()
else:
    def input():
        return next(stdin)[:-1]


    def inputi():
        return stdin.buffer.readline()

def bitcount(m):
    return bin(m).count('1')


def main():
    n,x,y = map(int, input().split())
    if x > y:
        x,y = y, x
    assert x <= y
    mm1 = range(1, 1 << y, 2)
    vbases = [((~(m1 >> (y - x)) & ~m1 & ((1 << x) - 1)) << y) | m1 for m1 in mm1 if m1 & m1 >> x == 0]
    def btail(m):
        return bitcount(m & ((1 << n % (x + y)) - 1))
    res = max(bitcount(m)*(n//(x+y)) + btail(m) for m in vbases)
    print(res)


if __name__ == "__main__":
    main()

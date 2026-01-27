import math

t = int(input())


def eval_(n, k):
    level = 0.5*math.log2(3*k+1)
    if n > 30:
        cond = (level - n) > 0
    else:
        cond = (3*k+1) > 4**n
    if cond:
        return "NO"
    elif n == 2 and k == 3:
        return "NO"
    else:
        level = math.floor(level)
        # print(level)
        if n > 5:
            # return "YES " +  str(n - level)
            temp = 1 + 0.5*math.log2(3*(k-1) + 1)
            if n > temp:
                return "YES " + str(n - 1)
            else:
                return "YES  0"
        else:
            delta = 2**(n-level)*(2**level-1)*(4**(n-level)-1)//3
            start = (4**(level)-1)//3
            if k <=(start+delta):
                return "YES " + str(n - level)
            else:
                return "YES " + str(n - level-1)



for i in range(t):
    (n, k) = [int(i) for i in input().split()]
    print(eval_(n, k))
#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import stdout

ask_count = 0
#a = [0,1,0,1,2,3,4,5,4,3,2,1,0,1,2,1]
#a = [-1, -2, -1, -2, -3, -2, -1, 0, 1, 0, -1, 0, 1, 0, 1, 2, 1, 0, 1, 0, 1, 0, 1, 0, -1, -2, -1, -2, -3, -4, -5, -6, -5, -6, -7, -6, -5, -4, -3, -2, -1, -2, -3, -4, -3, -4, -3, -4, -3, -2, -3, -4, -5, -6, -7, -6, -7, -6, -5, -6, -7, -6, -5, -6, -7, -6, -7, -8, -7, -6, -7, -6, -5, -6, -5, -4, -3, -4, -3, -2, -1, -2, -1, 0, 1, 2, 1, 0, -1, -2, -1, 0, 1, 2, 1, 0, 1, 0, 1, 0]
#n = len(a)
#print("n", n)
n = int(input())



def ask(num):
    global ask_count
    print("? " + str(num))
    stdout.flush()
    ask_count += 1
    return int(input())
    #return a[num-1]

def ans(num):
    print("! " + str(num))
    stdout.flush()

def opposite(num):
    return num + n // 2

low = 1
high = opposite(low)
lval = ask(low)
hval = ask(high)
prev_l_less_h = (lval < hval)
#print(prev_l_less_h)


while high - low > 1:
    #print("low", low, ";high", high)
    mid = (low + high) // 2

    lval = ask(mid)
    hval = ask(opposite(mid))
    l_less_h = (lval < hval)

    if abs(lval - hval) % 2 == 1:
        ans(-1)
        exit(0)
    elif hval == lval:
        ans(mid)
        exit(0)
    else:
        if l_less_h == prev_l_less_h:
            low = mid
        else:
            high = mid
ans(-1)
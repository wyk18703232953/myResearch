# -*- coding: utf-8 -*-
"""
@Project : CodeForces
@File    : 1.py 
@Time    : 2018/6/19 14:40
@Author  : Koushiro 
"""


if __name__ == "__main__":
    x,k = map(int, input().split())
    # y=2**k*(2*x-1)+1
    if x==0:  #
        print(0)
    else:
        y=pow(2,k,1000000007)*(2*x-1)+1
        result=int(y%(1000000007))  #
        print(result)

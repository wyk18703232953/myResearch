import math, sys, bisect, heapq, os
from collections import defaultdict, Counter, deque
from itertools import groupby, accumulate
from functools import lru_cache
import random

pr = lambda x: x
def aj_from_list(it):
    return list(map(int, next(it).split()))

def list3d(a, b, c, d):
    return [[[d] * c for _ in range(b)] for _ in range(a)]

def Y(c):
    print(["NO", "YES"][c])

def y(c):
    print(["no", "yes"][c])

def Yy(c):
    print(["No", "Yes"][c])

def solve_given_array(A):
    n = len(A)
    if A.count(0) >= 2:
        print('cslnb')
    elif n == 1:
        if A[0] % 2:
            print('sjfnb')
        else:
            print('cslnb')
    else:
        g2 = 0
        flag = 1
        C = Counter(A)
        for i in C.keys():
            if C[i] >= 3:
                flag = 0
            if C[i] == 2 and C[i - 1] >= 1:
                flag = 0
            if C[i] == 2:
                g2 += 1
        if g2 >= 2:
            flag = 0
        if not flag:
            print('cslnb')
        else:
            movescount = 0
            A.sort()
            for ii, i in enumerate(A):
                movescount += i - ii
            if movescount % 2 == 0:
                print('cslnb')
            else:
                print('sjfnb')

def generate_test_data(n):
    # 生成规模为 n 的测试数组 A
    # 这里简单生成 0 到 n 之间的随机非负整数
    random.seed(0)
    A = [random.randint(0, n) for _ in range(n)]
    return A

def main(n):
    A = generate_test_data(n)
    solve_given_array(A)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)
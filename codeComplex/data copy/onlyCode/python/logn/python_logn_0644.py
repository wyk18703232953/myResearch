import collections
import random
import heapq
import bisect
import math
import time
# import operator as op
# from functools import reduce

class Solution2:

    def solve(self, s):
        pass
        

class Solution:

    def solve(self, n, k):
        
        grow = 1
        tot = 0

        while n != tot - k:
            tot += grow
            grow += 1
            n -= 1
        return tot - k


sol = Solution()
sol2 = Solution2()


#TT = int(input())
for test_case in range(1):
    N, K = input().split()
    # s = []
    # for _ in range(int(N)):
    #     s.append(int(input()))

    out = sol.solve(int(N),int(K))
    print(str(out))
    #print("Case #" + str(test_case+1) + ": " + str(out))

    # out2 = sol2.solve(s)
    # print("Case #" + str(i+1) + ": " + str(out2))


# for _ in range(100000):
#     rand = [random.randrange(60) for _ in range(10)]
#     out1 = sol.solve(rand)
#     out2 = sol2.solve(rand)
#     if out1 != out2: 
#         print(rand, out1, out2)
#         break
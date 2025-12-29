# Transformed version of the original program:
# - No input()
# - Logic wrapped in main(n)
# - main(n) generates test data based on n and calls solve

import heapq
from heapq import heappush as push_
from heapq import heappop as pop_
import random

class heapT:
    def __init__(self, T):
        self.Q = []
        self.curT = 0
        self.maxT = T
        self.his = []

    def push(self, t, index):
        push_(self.Q, (-t, index))
        self.his.append(index)
        self.curT += t

        while self.curT > self.maxT:
            self.pop()

    def pop(self):
        t, ind = pop_(self.Q)
        self.his.append(ind)
        self.curT -= -t

    def normalize(self, length):
        while len(self.Q) > length:
            self.pop()

def solve(a, n, T):
    a = sorted(a, key=lambda x: x[0], reverse=True)
    H = heapT(T)

    max_ = -1
    pos = None

    for ak, t, ind in a:
        H.push(t, ind)
        H.normalize(ak)

        if len(H.Q) > max_:
            max_ = len(H.Q)
            pos = len(H.his)

    d = {}
    if pos is not None:
        for x in H.his[:pos]:
            if x not in d:
                d[x] = 1
            else:
                del d[x]

    if len(d) > 0:
        print(len(d))
        print(len(d))
        print(' '.join(str(x + 1) for x in d))
    else:
        print('0')
        print('0')

def main(n):
    # Generate test data for size n
    # Task: choose up to a_i tasks, each taking t_i time, within total time T.
    # We generate:
    # - a_i in [1, n]
    # - t_i in [1, 1000]
    # - T around n * average t (looser bound so solution is non-trivial)

    random.seed(0)
    max_time_per_task = 1000
    T = max(1, n * max_time_per_task // 2)

    a = []
    for i in range(n):
        ak = random.randint(1, n)
        t = random.randint(1, max_time_per_task)
        a.append([ak, t, i])

    solve(a, n, T)

# Example call (you can change n as needed)
if __name__ == "__main__":
    main(5)
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def cint(c):
    return ord(c) - 96
####################################################

def find_min_weight(n, k, stages):
    n = len(stages)
    min_weight = float('inf')

    def backtrack(s, w, t):
        nonlocal min_weight 

        if t >= k:
            min_weight = min(min_weight, w)
            return

        if s >= n - 1:
            return

        for i in range(s+1, n, 1):
            if stages[i] - stages[s] > 1:
                backtrack(i, w+stages[i], t+1)

    backtrack(0, stages[0], 1)

    if min_weight == float('inf'):
        return -1

    return min_weight    


n, k = inlt()
stages = list(set(map(cint, insr())))
stages.sort()
print(find_min_weight(n, k, stages))

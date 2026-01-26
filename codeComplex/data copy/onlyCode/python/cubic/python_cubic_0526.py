import sys
import bisect

ls2int = lambda ls: int(''.join(map(str,ls)))
def candidates(digs, num):
    if not digs:
        return [[]]
    
    res = []
    i = bisect.bisect_left(digs, num[0])
    
    # lead with same digit
    if num[0] in digs:
        for suffix in candidates(digs[:i]+digs[i+1:], num[1:]):
            res.append([digs[i]] + suffix)
    
    # lead with next smallest digit:
    if i > 0:
        i -= 1
        res.append([digs[i]] + list(reversed(digs[:i]+digs[i+1:])))
    
    return res
    
def solution(a, b):
    digits = [int(x) for x in sorted(a)]
    ceiling = [int(x) for x in b]
    
    assert(len(digits) <= len(ceiling), 'solution does not exist')
    if len(digits) < len(ceiling):
        return ls2int(digits[::-1])
    return max(ls2int(ls) for ls in candidates(digits, ceiling))
    
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
print(solution(a, b))
from collections import defaultdict as dd
from collections import deque, Counter
import bisect
import heapq
from math import inf

import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        import os
        self.os = os
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            self.os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


def ri():
    return int(input())
 
def rl():
    return list(map(int, input().split()))


 
n, m = rl()
aa = rl()

#convert aa to array of [+,-,-,-,+,-,+,....]
bb = [-1]*n
for i in range(n):
	if aa[i] == m:
	    bb[i] = 1
	elif aa[i] < m:
	    bb[i] = -1
	else: # aa[i] > m
	    bb[i] = 1

prefix_sum= [0]*(n+1)
for i in range(1, n+1):
    prefix_sum[i] = bb[i-1] + prefix_sum[i-1]


#now if we choose l and r, we have to compare:
# median on [l,r] more or equal to m iff (prefix_sum[r+1] - prefix_sum[l]) > 0  (1)

#if we do the same thing with m+1 instead of m
#median on [l,r] more or equal to m +1 ...

#we can deduct second result from first\
#to get the number of pairs [l,r] such as \
#median on [l,r] exactly equal to m


#we can rewrite (1)  as prefix_sum[r+1] > prefix_sum[l]
#this is linked to counting the number of inversions in the prefix sum!!
#classic problem, can be done by merge sort

#we need to be a bit carefull, because we want only the inversions\
# with l on left of median and r on the right
# can count inversion on 3 parts:
#-whole array
#-begin of array to median
#-median to end
#then deduct the last two from the first

def mergeSortGoodOrder(arr):
    """
    this doesn t count the number of inversions, but quite the opposite
    it counts the number of pairs i < j such as arr[i] < arr[j]
    """
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]        

        a, ai = mergeSortGoodOrder(a)
        b, bi = mergeSortGoodOrder(b)
        c = []        

        i = 0
        j = 0
        good = 0 + ai + bi    

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
            good += (len(b)-j)
        else:
            c.append(b[j])
            j += 1
               

    c += a[i:]
    c += b[j:]

    return c, good



#step1: with m


#we want prefix_sum[l] < prefix_sum[r+1]
#ie : prefix_sum[l] < prefix_sum[r], and r stricly on the right of median


#find position of median
idx = 0
for i in range(n):
    if aa[i] == m:
        idx = i


_, good = mergeSortGoodOrder(prefix_sum)

_, bad_left = mergeSortGoodOrder(prefix_sum[:idx + 1])

_, bad_right = mergeSortGoodOrder(prefix_sum[idx + 1:])


first_count = good - bad_left - bad_right

#step2: with m + 1
bb = [-1]*n
for i in range(n):
	if aa[i] == m + 1:
	    bb[i] = 1
	elif aa[i] < m + 1:
	    bb[i] = -1
	else: # aa[i] > m + 1
	    bb[i] = 1

prefix_sum= [0]*(n+1)
for i in range(1, n+1):
    prefix_sum[i] = bb[i-1] + prefix_sum[i-1]



##BE CAREFUL: here we need to keep idx as the one of aa[idx] = m, NOT aa[idx = m+1]
# #find position of m + 1
# idx = 0
# for i in range(n):
#     if aa[i] == m + 1:
#         idx = i


_, good = mergeSortGoodOrder(prefix_sum)

_, bad_left = mergeSortGoodOrder(prefix_sum[:idx + 1])

_, bad_right = mergeSortGoodOrder(prefix_sum[idx + 1:])

second_count = good - bad_left - bad_right


#step3: combine

ans   = first_count - second_count

print(ans)



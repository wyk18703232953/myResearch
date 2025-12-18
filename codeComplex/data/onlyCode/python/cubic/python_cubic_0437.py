# from typing import List, Set, Dict, Tuple, Text, Optional
from collections import deque
from types import GeneratorType
import os
import sys
import math
import heapq
from atexit import register
from io import BytesIO
import __pypy__  # type: ignore

#########
# INPUT #
#########


class Input(object):
  def __init__(self):
    if 'CPH' not in os.environ:
      sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
      sys.stdout = BytesIO()
      register(lambda: os.write(1, sys.stdout.getvalue()))

  def rawInput(self):
    # type: () -> str
    return sys.stdin.readline().rstrip('\r\n')

  def readInt(self):
    return int(self.rawInput())

##########
# OUTPUT #
##########


class Output(object):
  def __init__(self):
    self.out = __pypy__.builders.StringBuilder()

  def write(self, text):
    # type: (str) -> None
    self.out.append(str(text))

  def writeLine(self, text):
    # type: (str) -> None
    self.write(str(text) + '\n')

  def finalize(self):
    if sys.version_info[0] < 3:
      os.write(1, self.out.build())
    else:
      os.write(1, self.out.build().encode())

###########
# LIBRARY #
###########


def bootstrap(f, stack=[]):
  # Deep Recursion helper.
  # From: https://github.com/cheran-senthil/PyRival/blob/c1972da95d102d95b9fea7c5c8e0474d61a54378/docs/bootstrap.rst
  # Usage:

  # @bootstrap
  # def recur(n):
  #   if n == 0:
  #     yield 1
  #   yield (yield recur(n-1)) * n
  def wrappedfunc(*args, **kwargs):
    if stack:
      return f(*args, **kwargs)
    else:
      to = f(*args, **kwargs)
      while True:
        if type(to) is GeneratorType:
          stack.append(to)
          to = next(to)
        else:
          stack.pop()
          if not stack:
            break
          to = stack[-1].send(to)
      return to

  return wrappedfunc


'''
arrayInit([3, 4, 5], 0):
Initialize 3-dim array with [3][4][5] with 0 as its initial value

Tested with:
https://codeforces.com/contest/625/problem/B
'''


class MDArray(object):
  # Faster implementation of md array, using a single array and a lot of math.
  '''
  >>> x = MDArray([1, 2, 5], 5)
  >>> x.get([0, 0, 0])
  5
  >>> x.get([0, 1, 4])
  5
  >>> x.set([0, 1, 2], 3)
  3
  >>> x.get([0, 1, 4])
  5
  >>> x.get([0, 1, 2])
  3
  >>> x.set([0, 1, 3], 1)
  1
  >>> x.get([0, 1, 4])
  5
  >>> x.get([0, 1, 2])
  3
  >>> x.get([0, 1, 3])
  1
  '''

  def __init__(self, dimensions, initial_value=0):
    # type: (Iterable[int], Any) -> None
    self.dimensions = dimensions
    dim_total = 1
    for i in dimensions:
      dim_total *= i
    self.arr = [initial_value] * dim_total

  def _index(self, indexes):
    assert len(indexes) == len(self.dimensions)
    idx_multi = 1
    idx = 0
    for i in range(len(indexes)):
      assert 0 <= indexes[i] < self.dimensions[i]
      idx += indexes[i] * idx_multi
      idx_multi *= self.dimensions[i]
    return idx

  def get(self, indexes):
    # type: (Iterable[int]) -> Any
    return self.arr[self._index(indexes)]

  def set(self, indexes, value):
    # type: (Iterable[int], Any) -> Any
    self.arr[self._index(indexes)] = value
    return value


#########
# LOGIC #
#########

def encode(row, col, n, m):
  return row * m + col


def solve(node, remain, adj, dp, n, m):
  if remain == 0:
    return 0

  key = (node + remain * n * m)
  mem = dp[key]
  if mem != -1:
    return mem

  ans = min(map(lambda x: solve(x[0], remain-1,
            adj, dp, n, m) + x[1], adj[node]))
  dp[key] = ans
  return ans


def main(inp, out):
  # type: (Input, Output) -> any
  n, m, k = map(int, inp.rawInput().split())
  if k % 2 == 1:
    for _ in range(n):
      out.writeLine(' '.join(map(str, [-1] * m)))
    return

  total_nodes = n*m
  adj = [[] for _ in range(total_nodes)]

  for i in range(n):
    weights = map(int, inp.rawInput().split())
    for j in range(m-1):
      cur = encode(i, j, n, m)
      nex = encode(i, j+1, n, m)
      adj[cur].append((nex, weights[j]))
      adj[nex].append((cur, weights[j]))

  for i in range(n-1):
    weights = map(int, inp.rawInput().split())
    for j in range(m):
      cur = encode(i, j, n, m)
      nex = encode(i+1, j, n, m)
      adj[cur].append((nex, weights[j]))
      adj[nex].append((cur, weights[j]))

  dp = [-1] * (n*m*(k/2+1))

  for i in range(n):
    ans = []
    for j in range(m):
      node = encode(i, j, n, m)
      ans.append(solve(node, k/2, adj, dp, n, m) * 2)
    out.writeLine(' '.join(map(str, ans)))


###############
# BOILERPLATE #
###############

output_obj = Output()
main(Input(), output_obj)
output_obj.finalize()

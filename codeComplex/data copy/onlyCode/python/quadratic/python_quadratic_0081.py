# from typing import List, Set, Dict, Tuple, Text, Optional
from collections import deque
from types import GeneratorType
import os
import sys
import math
import heapq
import functools
import random
from atexit import register
from io import BytesIO
import __pypy__  # type: ignore

EPS = 10**-12

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


class CycleFindDirected(object):
  '''
  >>> tp = CycleFindDirected(6)
  >>> tp.find() is None
  True
  >>> tp.add_edge(1, 2)
  >>> tp.add_edge(2, 4)
  >>> tp.add_edge(2, 3)
  >>> tp.add_edge(3, 0)
  >>> tp.add_edge(1, 3)
  >>> tp.find() is None
  True
  >>> tp.add_edge(0, 1)
  >>> len(tp.find())
  4
  >>> tp.add_edge(3, 1)
  >>> tp.find() is not None
  True
  >>> tp = CycleFindDirected(2)
  >>> tp.add_edge(0, 1)
  >>> tp.add_edge(1, 1)
  >>> tp.find()
  [1, 1]
  >>> tp = CycleFindDirected(2)
  >>> tp.add_edge(0, 1)
  >>> tp.add_edge(1, 0)
  >>> tp.find() in [[0, 1], [1, 0]]
  True

  Tested in: 
  '''

  def __init__(self, n):
    # type: (int) -> None
    self.n = n
    self.adj = [[] for _ in range(n)]

  def add_edge(self, u, v):
    # type: (int, int) -> None
    assert 0 <= u < self.n
    assert 0 <= v < self.n
    self.adj[u].append(v)

  @bootstrap
  def dfs(self, node):
    self.color[node] = 1
    for i in self.adj[node]:
      if self.color[i] == 0:
        # unvisited
        self.parent[i] = node
        if (yield self.dfs(i)):
          yield True

      elif self.color[i] == 1:
        self.cycle_end = node
        self.cycle_start = i
        yield True

    self.color[node] = 2
    yield False

  def find(self):
    self.color = [0] * self.n
    self.parent = [-1] * self.n
    self.cycle_end = -1
    self.cycle_start = -1

    for i in range(self.n):
      if not self.color[i] and self.dfs(i):
        answer = []
        node_begin = self.cycle_start
        node_end = self.cycle_end
        answer.append(node_begin)
        while node_end != node_begin:
          answer.append(node_end)
          node_end = self.parent[node_end]

        answer.reverse()
        if len(answer) == 1:
          # special case of self loop
          return [node_begin, node_begin]
        return answer

    return None


#########
# LOGIC #
#########


def main(inp, out):
  # type: (Input, Output) -> any
  n, m = map(int, inp.rawInput().split())
  edges = []
  base = CycleFindDirected(n)
  for _ in range(m):
    u, v = map(int, inp.rawInput().split())
    u -= 1
    v -= 1
    edges.append((u, v))
    base.add_edge(u, v)

  cycle = base.find()
  if not cycle:
    out.writeLine("YES")
    return

  cycle.append(cycle[0])

  bad_edges = set()
  cycle_edges = []
  for u, v in zip(cycle[:-1], cycle[1:]):
    bad_edges.add((u, v))
    cycle_edges.append((u, v))

  cf = CycleFindDirected(n)
  for edge in edges:
    if edge not in bad_edges:
      cf.add_edge(edge[0], edge[1])

  for edge in cycle_edges:
    for toadd in cycle_edges:
      if toadd != edge:
        cf.adj[toadd[0]].append(toadd[1])

    if not cf.find():
      out.writeLine('YES')
      return

    for toadd in cycle_edges:
      if toadd != edge:
        cf.adj[toadd[0]].pop()

  out.writeLine('NO')

###############
# BOILERPLATE #
###############


output_obj = Output()
main(Input(), output_obj)
output_obj.finalize()

import sys, os, io
import math, datetime, functools, itertools, operator, bisect, fractions, statistics
from collections import deque, defaultdict, OrderedDict, Counter
from fractions import Fraction
from decimal import Decimal
from heapq import heappush, heappop, heapify, _heapify_max, _heappop_max, nsmallest, nlargest

def main(n):
    # n 表示每个测试用例中数组的长度
    # 生成确定性的多测试用例数据：这里设定测试用例数量为 T = 3
    tc = 3
    outputs = []
    for t in range(tc):
        length = n

        # 生成确定性数组 a，长度为 length
        # 使用简单算术构造，保证可重复：
        # 第 t 个测试用例的第 i 个元素为 (i % (2 * (t + 2))) + (t + 1)
        a = [(i % (2 * (t + 2))) + (t + 1) for i in range(length)]

        d = Counter(a)
        a_unique_sorted = sorted(list(set(a)))
        s = []
        c = 0
        for i in a_unique_sorted:
            if d[i] >= 4:
                c = 1
                outputs.append(f"{i} {i} {i} {i}")
                break
            if d[i] >= 2:
                s.append(i)
        if c == 0:
            lx = 9999999999999999999999999999999
            bx = 1
            for i in range(len(s) - 1):
                l = s[i + 1]
                b = s[i]
                if l * bx < lx * b:
                    lx = l
                    bx = b
            outputs.append(f"{lx} {lx} {bx} {bx}")
    sys.stdout.write("\n".join(outputs) + "\n")

class FastReader(io.IOBase):
    newlines = 0
    def __init__(self, fd, chunk_size=1024 * 8):
        self._fd = fd
        self._chunk_size = chunk_size
        self.buffer = io.BytesIO()
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, self._chunk_size))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self, size=-1):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, self._chunk_size if size == -1 else size))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

class FastWriter(io.IOBase):
    def __init__(self, fd):
        self._fd = fd
        self.buffer = io.BytesIO()
        self.write = self.buffer.write
    def flush(self):
        os.write(self._fd, self.buffer.getvalue())
        self.buffer.truncate(0), self.buffer.seek(0)

class FastStdin(io.IOBase):
    def __init__(self, fd=0):
        self.buffer = FastReader(fd)
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

class FastStdout(io.IOBase):
    def __init__(self, fd=1):
        self.buffer = FastWriter(fd)
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.flush = self.buffer.flush

if __name__ == "__main__":
    sys.stdin = FastStdin()
    sys.stdout = FastStdout()
    main(10)
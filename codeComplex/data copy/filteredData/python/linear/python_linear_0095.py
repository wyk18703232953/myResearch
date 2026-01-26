import sys, os, io
import math, datetime, functools, itertools, operator, bisect, fractions, statistics
from collections import deque, defaultdict, OrderedDict, Counter
from fractions import Fraction
from decimal import Decimal
from sys import stdout
from heapq import heappush, heappop, heapify, _heapify_max, _heappop_max, nsmallest, nlargest

INF = 99999999999999999999999999999999

class SortedList:
    def __init__(self, iterable=[], _load=200):
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def _fen_build(self):
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False

    def _fen_update(self, index, value):
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        if self._rebuild:
            self._fen_build()
        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x

    def _fen_findkth(self, k):
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return 0, k
        if k >= self._len - _list_lens[-1]:
            return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild:
            self._fen_build()
        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k

    def _delete(self, pos, idx):
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens
        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1
        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]

        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True

    def _loc_left(self, value):
        if not self._len:
            return 0, 0
        _lists = self._lists
        _mins = self._mins
        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi

            else:
                lo = mi
        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1
        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi

            else:
                lo = mi
        return pos, idx

    def _loc_right(self, value):
        if not self._len:
            return 0, 0
        _lists = self._lists
        _mins = self._mins
        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi

            else:
                pos = mi
        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi

            else:
                lo = mi
        return pos, idx

    def add(self, value):
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens
        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True

        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True

    def discard(self, value):
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)

    def remove(self, value):
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))

    def pop(self, index=-1):
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def bisect_left(self, value):
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        return self.bisect_right(value) - self.bisect_left(value)

    def __len__(self):
        return self._len

    def __getitem__(self, index):
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]

    def __delitem__(self, index):
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)

    def __contains__(self, value):
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False

    def __iter__(self):
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        return (value for _list in reversed(self._lists) for value in reversed(_list))

    def __repr__(self):
        return 'SortedList({0})'.format(list(self))

def main(n):
    mod = 1000000007
    starttime = datetime.datetime(2000, 1, 1)

    # 输入结构：原程序是单测例，读取一个整数 n 和一个长度为 n 的字符串 s
    # 这里将 n 视为字符串长度规模
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性构造长度为 n 的字符串 s
    # 使用周期性的小写字母序列
    chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = ''.join(chars)

    # 核心逻辑保持不变
    d = {}
    for i in range(n):
        d[s[i]] = 1

    l = 0
    r = 0
    td = {}
    ans = INF
    while l <= r and r < n:
        while len(td) != len(d):
            if r == n:
                # print(ans)
                pass
                return
            if s[r] in td:
                td[s[r]] += 1

            else:
                td[s[r]] = 1
            r += 1

        if len(td) == len(d):
            r -= 1
            ans = min(ans, r - l + 1)
        while l <= r:
            td[s[l]] -= 1
            if td[s[l]] == 0:
                del td[s[l]]
                ans = min(ans, r - l + 1)
                l += 1
                break
            l += 1
        r += 1

    # print(ans)
    pass

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
    # 示例调用：输入规模 n
    main(1000)
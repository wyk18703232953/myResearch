import math
from collections import Counter

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
 
    def __len__(self):
        return self._len
 
    def __getitem__(self, index):
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]
 
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


def core_algorithm(a, b):
    if len(a) < len(b):
        return ''.join(sorted(a)[::-1])

    else:
        a_sorted = sorted(a)
        ans = []
        sa = SortedList(a_sorted)
        for i in range(len(a_sorted) - 1):
            for j in range(len(sa) - 1, -1, -1):
                temp = ans + [sa[j]]
                sa.discard(sa[j])
                for k in sa:
                    temp.append(k)
                if temp <= b:
                    ans.append(temp[i])
                    break

                else:
                    sa.add(temp[i])
        ans.append(sa[-1])
        return "".join(ans)


def generate_strings(n):
    # Generate two strings a and b based on n
    # Let length of a be n, and length of b be n (to trigger main branch often)
    # Characters are deterministic cycle over 'a'..'z'
    alph = "abcdefghijklmnopqrstuvwxyz"
    la = n
    lb = n
    a = [alph[(i * 7) % 26] for i in range(la)]
    b = [alph[(i * 5 + 3) % 26] for i in range(lb)]
    return a, b


def main(n):
    a, b = generate_strings(n)
    b_list = list(b)
    result = core_algorithm(list(a), b_list)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)
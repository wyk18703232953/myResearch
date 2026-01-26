import math
from collections import Counter

MOD = 10**9 + 7

class SegmentTree:
    def __init__(self, data, default=0, func=lambda a, b: max(a, b)):
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        if start == stop:
            return self.__getitem__(start)
        stop += 1
        start += self._size
        stop += self._size
        res = self._default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

class SegmentTree1:
    def __init__(self, data, default=0, func=lambda a, b: a + b):
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        if start == stop:
            return self.__getitem__(start)
        stop += 1
        start += self._size
        stop += self._size
        res = self._default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

MOD = 10**9 + 7
omod = 998244353

prime = [True for _ in range(11)]
prime[0] = prime[1] = False

def SieveOfEratosthenes(n=10):
    p = 2
    c = 0
    while p <= n:
        if prime[p]:
            c += 1
            for i in range(p, n + 1, p):
                prime[i] = False
        p += 1

class DSU:
    def __init__(self, R, C):
        self.par = list(range(R * C + 1))
        self.rnk = [0] * (R * C + 1)
        self.sz = [1] * (R * C + 1)

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]

    def size(self, x):
        return self.sz[self.find(x)]

    def top(self):
        return self.size(len(self.sz) - 1) - 1

class LazySegTree:
    def __init__(self, _op, _e, _mapping, _composition, _id, v):
        def set_func(p, x):
            assert 0 <= p < _n
            p_local = p + _size
            for i in range(_log, 0, -1):
                _push(p_local >> i)
            _d[p_local] = x
            for i in range(1, _log + 1):
                _update(p_local >> i)

        def get_func(p):
            assert 0 <= p < _n
            p_local = p + _size
            for i in range(_log, 0, -1):
                _push(p_local >> i)
            return _d[p_local]

        def prod_func(l, r):
            assert 0 <= l <= r <= _n
            if l == r:
                return _e
            l_local = l + _size
            r_local = r + _size
            for i in range(_log, 0, -1):
                if ((l_local >> i) << i) != l_local:
                    _push(l_local >> i)
                if ((r_local >> i) << i) != r_local:
                    _push(r_local >> i)
            sml = _e
            smr = _e
            while l_local < r_local:
                if l_local & 1:
                    sml = _op(sml, _d[l_local])
                    l_local += 1
                if r_local & 1:
                    r_local -= 1
                    smr = _op(_d[r_local], smr)
                l_local >>= 1
                r_local >>= 1
            return _op(sml, smr)

        def apply_func(l, r, f):
            assert 0 <= l <= r <= _n
            if l == r:
                return
            l_local = l + _size
            r_local = r + _size
            for i in range(_log, 0, -1):
                if ((l_local >> i) << i) != l_local:
                    _push(l_local >> i)
                if ((r_local >> i) << i) != r_local:
                    _push((r_local - 1) >> i)
            l2 = l_local
            r2 = r_local
            while l_local < r_local:
                if l_local & 1:
                    _all_apply(l_local, f)
                    l_local += 1
                if r_local & 1:
                    r_local -= 1
                    _all_apply(r_local, f)
                l_local >>= 1
                r_local >>= 1
            l_local = l2
            r_local = r2
            for i in range(1, _log + 1):
                if ((l_local >> i) << i) != l_local:
                    _update(l_local >> i)
                if ((r_local >> i) << i) != r_local:
                    _update((r_local - 1) >> i)

        def _update(k):
            _d[k] = _op(_d[2 * k], _d[2 * k + 1])

        def _all_apply(k, f):
            _d[k] = _mapping(f, _d[k])
            if k < _size:
                _lz[k] = _composition(f, _lz[k])

        def _push(k):
            _all_apply(2 * k, _lz[k])
            _all_apply(2 * k + 1, _lz[k])
            _lz[k] = _id

        _n = len(v)
        _log = _n.bit_length()
        _size = 1 << _log
        _d = [_e] * (2 * _size)
        _lz = [_id] * _size
        for i in range(_n):
            _d[_size + i] = v[i]
        for i in range(_size - 1, 0, -1):
            _update(i)

        self.set = set_func
        self.get = get_func
        self.prod = prod_func
        self.apply = apply_func

MIL = 1 << 20

def makeNode(total, count):
    return (total * MIL) + count

def getTotal(node):
    return math.floor(node / MIL)

def getCount(node):
    return node - getTotal(node) * MIL

nodeIdentity = makeNode(0.0, 0.0)

def nodeOp(node1, node2):
    return node1 + node2
    return makeNode(
        getTotal(node1) + getTotal(node2), getCount(node1) + getCount(node2)
    )

identityMapping = -1

def mapping(tag, node):
    if tag == identityMapping:
        return node
    count = getCount(node)
    return makeNode(tag * count, count)

def composition(mapping1, mapping2):
    return mapping1 if mapping1 != identityMapping else mapping2

def memodict(f):
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__

def pollard_rho(n):
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            prev = p
            p = (p * p) % n
            if p == 1:
                return math.gcd(prev - 1, n)
            if p == n - 1:
                break
        else:
            for i in range(2, n):
                x = i
                y = (i * i + 1) % n
                f = math.gcd(abs(x - y), n)
                while f == 1:
                    x = (x * x + 1) % n
                    y = (y * y + 1) % n
                    y = (y * y + 1) % n
                    f = math.gcd(abs(x - y), n)
                if f != n:
                    return f
    return n

@memodict
def prime_factors(n):
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)

def distinct_factors(n):
    factors = [1]
    for p, exp in prime_factors(n).items():
        factors += [p**i * factor for factor in factors for i in range(1, exp + 1)]
    return factors

def all_factors(n):
    small = []
    large = []
    step = 2 if n & 1 else 1
    for i in range(1, int(n**0.5) + 1, step):
        if not n % i:
            small.append(i)
            large.append(n // i)
    if small and large and small[-1] == large[-1]:
        large.pop()
    large.reverse()
    small.extend(large)
    return small

def binarySearch(arr, n, key):
    left = 0
    right = n - 1
    mid = 0
    res = n
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] > key:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

def binarySearch1(arr, n, key):
    left = 0
    right = n - 1
    mid = 0
    res = -1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] > key:
            right = mid - 1
        else:
            res = mid
            left = mid + 1
    return res

def core_algorithm(a):
    limit = 10**5
    size_twopow = limit + 69
    twopow = [1] * size_twopow
    for i in range(1, size_twopow):
        twopow[i] = (twopow[i - 1] * 2) % MOD
    size_count = 100069
    count = [0] * size_count
    for v in a:
        if 0 <= v < size_count:
            count[v] += 1
    multiples = [0] * size_count
    for i in range(1, limit + 1):
        s = 0
        for j in range(i, limit + 1, i):
            s += count[j]
        multiples[i] = s
    gcd_of = [0] * size_count
    for i in range(limit, 0, -1):
        val = (twopow[multiples[i]] - 1) % MOD
        j = 2 * i
        while j <= limit:
            val -= gcd_of[j]
            j += i
        gcd_of[i] = val
    return gcd_of[1] % MOD

def generate_input_array(n):
    if n <= 0:
        return []
    max_val = 10**5
    arr = [1 + (i * 9973 + 12345) % max_val for i in range(n)]
    return arr

def main(n):
    a = generate_input_array(n)
    result = core_algorithm(a)
    print(result)

if __name__ == "__main__":
    main(10)
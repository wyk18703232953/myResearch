import math

MOD = 998244353

class SegmentTree:
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

class SegmentTree1:
    def __init__(self, data, default=10 ** 6, func=lambda a, b: min(a, b)):
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

class Factorial:
    def __init__(self, MOD):
        self.MOD = MOD
        self.factorials = [1, 1]
        self.invModulos = [0, 1]
        self.invFactorial_ = [1, 1]

    def calc(self, n):
        if n <= -1:
            raise ValueError("n must be non-negative")
        if n < len(self.factorials):
            return self.factorials[n]
        nextArr = [0] * (n + 1 - len(self.factorials))
        initialI = len(self.factorials)
        prev = self.factorials[-1]
        m = self.MOD
        for i in range(initialI, n + 1):
            prev = nextArr[i - initialI] = prev * i % m
        self.factorials += nextArr
        return self.factorials[n]

    def inv(self, n):
        if n <= -1:
            raise ValueError("n must be non-negative")
        p = self.MOD
        pi = n % p
        if pi < len(self.invModulos):
            return self.invModulos[pi]
        initialI = len(self.invModulos)
        for i in range(initialI, min(p, n + 1)):
            nxt = -self.invModulos[p % i] * (p // i) % p
            self.invModulos.append(nxt)
        return self.invModulos[pi]

    def invFactorial(self, n):
        if n <= -1:
            raise ValueError("n must be non-negative")
        if n < len(self.invFactorial_):
            return self.invFactorial_[n]
        self.inv(n)
        nextArr = [0] * (n + 1 - len(self.invFactorial_)]
        initialI = len(self.invFactorial_)
        prev = self.invFactorial_[-1]
        p = self.MOD
        for i in range(initialI, n + 1):
            prev = nextArr[i - initialI] = (prev * self.invModulos[i % p]) % p
        self.invFactorial_ += nextArr
        return self.invFactorial_[n]

class Combination:
    def __init__(self, MOD):
        self.MOD = MOD
        self.factorial = Factorial(MOD)

    def ncr(self, n, k):
        if k < 0 or n < k:
            return 0
        k = min(k, n - k)
        f = self.factorial
        return f.calc(n) * f.invFactorial(max(n - k, k)) * f.invFactorial(min(k, n - k)) % self.MOD

class LazySegTree:
    def __init__(self, _op, _e, _mapping, _composition, _id, v):
        def set_(p, x):
            assert 0 <= p < _n
            p += _size
            for i in range(_log, 0, -1):
                _push(p >> i)
            _d[p] = x
            for i in range(1, _log + 1):
                _update(p >> i)

        def get_(p):
            assert 0 <= p < _n
            p += _size
            for i in range(_log, 0, -1):
                _push(p >> i)
            return _d[p]

        def prod_(l, r):
            assert 0 <= l <= r <= _n
            if l == r:
                return _e
            l += _size
            r += _size
            for i in range(_log, 0, -1):
                if ((l >> i) << i) != l:
                    _push(l >> i)
                if ((r >> i) << i) != r:
                    _push(r >> i)
            sml = _e
            smr = _e
            while l < r:
                if l & 1:
                    sml = _op(sml, _d[l])
                    l += 1
                if r & 1:
                    r -= 1
                    smr = _op(_d[r], smr)
                l >>= 1
                r >>= 1
            return _op(sml, smr)

        def apply_(l, r, f):
            assert 0 <= l <= r <= _n
            if l == r:
                return
            l += _size
            r += _size
            for i in range(_log, 0, -1):
                if ((l >> i) << i) != l:
                    _push(l >> i)
                if ((r >> i) << i) != r:
                    _push((r - 1) >> i)
            l2 = l
            r2 = r
            while l < r:
                if l & 1:
                    _all_apply(l, f)
                    l += 1
                if r & 1:
                    r -= 1
                    _all_apply(r, f)
                l >>= 1
                r >>= 1
            l = l2
            r = r2
            for i in range(1, _log + 1):
                if ((l >> i) << i) != l:
                    _update(l >> i)
                if ((r >> i) << i) != r:
                    _update((r - 1) >> i)

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

        self.set = set_
        self.get = get_
        self.prod = prod_
        self.apply = apply_

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

prime = [True for _ in range(10)]
pp = [0] * 10

def SieveOfEratosthenes(n=10):
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for i in range(p, n + 1, p):
                pp[i] += 1
                prime[i] = False
        p += 1

def binarySearch(arr, n, key):
    left = 0
    right = n - 1
    res = arr[n - 1]
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] >= key:
            res = arr[mid]
            right = mid - 1

        else:
            left = mid + 1
    return res

def binarySearch1(arr, n, key):
    left = 0
    right = n - 1
    res = arr[0]
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] > key:
            right = mid - 1

        else:
            res = arr[mid]
            left = mid + 1
    return res

def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    a = [(i * 3 + 1) % MOD for i in range(n)]
    difficulty = a[0]
    expectation = a[0] % MOD
    for i in range(1, n):
        expectation = expectation * 2 + difficulty + a[i]
        difficulty = difficulty * 2 + a[i]
        expectation %= MOD
        difficulty %= MOD
    # print(expectation)
    pass
if __name__ == "__main__":
    main(5)
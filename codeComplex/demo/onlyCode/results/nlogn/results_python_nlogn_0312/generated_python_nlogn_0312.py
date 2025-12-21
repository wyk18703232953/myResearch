class BIT:

    __all__ = ['add', 'sumrange', 'lower_left']

    def __init__(self, maxsize=10**7):
        assert (maxsize > 0)
        self._n = maxsize+1
        self._bitdata = [0]*(maxsize+1)

    def add(self, i, x):
        assert(0 <= i < self._n)
        pos = i+1
        while pos < self._n:
            self._bitdata[pos] += x
            pos += pos & (-pos)

    def running_total(self, i):
        assert (-1 <= i < self._n)
        if i == -1:
            return 0
        returnval = 0
        pos = i+1
        while pos:
            returnval += self._bitdata[pos]
            pos -= pos & (-pos)
        return returnval

    def sumrange(self, lo=0, hi=None):
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = self._n
        return self.running_total(hi) - self.running_total(lo-1)

    def lower_left(self, total):
        if total < 0:
            return -1
        pos = 0
        k = 1 << (self._n.bit_length() - 1)
        while k > 0:
            if pos + k < self._n and self._bitdata[pos + k] < total:
                total -= self._bitdata[pos + k]
                pos += k
            k //= 2
        return pos

def tentousu(lis):
    maxv = 0
    if lis:
        maxv = max(lis)
    bit = BIT(maxv + 2)
    ans = 0
    for i in range(len(lis)):
        bit.add(lis[i], 1)
        ans += i + 1 - bit.running_total(lis[i])
    return ans

def main(n):
    L = list(range(n))
    L.reverse()
    a = tentousu(L)
    a %= 2
    if n % 2 == 0 and a % 2 == 0:
        return "Petr"
    if n % 2 == 0 and a % 2 == 1:
        return "Um_nik"
    if n % 2 == 1 and a % 2 == 0:
        return "Um_nik"
    if n % 2 == 1 and a % 2 == 1:
        return "Petr"

if __name__ == "__main__":
    print(main(5))
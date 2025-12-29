import random
from collections import defaultdict

mod = 10 ** 9 + 7
mod1 = 998244353


class TreeNode:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
        self.num_left = 1
        self.num_total = 1


class AvlTree:

    def __init__(self):
        self._tree = None

    def add(self, k, v):
        if not self._tree:
            self._tree = TreeNode(k, v)
            return
        node = self._add(k, v)
        if node:
            self._rebalance(node)

    def _add(self, k, v):
        node = self._tree
        while node:
            if k < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(k, v)
                    node.left.parent = node
                    return node.left
            elif node.key < k:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(k, v)
                    node.right.parent = node
                    return node.right
            else:
                node.value = v
                return

    @staticmethod
    def get_height(x):
        return x.height if x else 0

    @staticmethod
    def get_num_total(x):
        return x.num_total if x else 0

    def _rebalance(self, node):

        n = node
        while n:
            lh = self.get_height(n.left)
            rh = self.get_height(n.right)
            n.height = max(lh, rh) + 1
            balance_factor = lh - rh
            n.num_total = 1 + self.get_num_total(n.left) + self.get_num_total(n.right)
            n.num_left = 1 + self.get_num_total(n.left)

            if balance_factor > 1:
                if self.get_height(n.left.left) < self.get_height(n.left.right):
                    self._rotate_left(n.left)
                self._rotate_right(n)
            elif balance_factor < -1:
                if self.get_height(n.right.right) < self.get_height(n.right.left):
                    self._rotate_right(n.right)
                self._rotate_left(n)
            else:
                n = n.parent

    def _remove_one(self, node):
        replacement = node.left or node.right
        if node.parent:
            if AvlTree._is_left(node):
                node.parent.left = replacement
            else:
                node.parent.right = replacement
            replacement.parent = node.parent
            node.parent = None
        else:
            self._tree = replacement
            replacement.parent = None
        node.left = None
        node.right = None
        node.parent = None
        self._rebalance(replacement)

    def _remove_leaf(self, node):
        if node.parent:
            if AvlTree._is_left(node):
                node.parent.left = None
            else:
                node.parent.right = None
            self._rebalance(node.parent)
        else:
            self._tree = None
        node.parent = None
        node.left = None
        node.right = None

    def remove(self, k):
        node = self._get_node(k)
        if not node:
            return
        if AvlTree._is_leaf(node):
            self._remove_leaf(node)
            return
        if node.left and node.right:
            nxt = AvlTree._get_next(node)
            node.key = nxt.key
            node.value = nxt.value
            if self._is_leaf(nxt):
                self._remove_leaf(nxt)
            else:
                self._remove_one(nxt)
            self._rebalance(node)
        else:
            self._remove_one(node)

    def get(self, k):
        node = self._get_node(k)
        return node.value if node else -1

    def _get_node(self, k):
        if not self._tree:
            return None
        node = self._tree
        while node:
            if k < node.key:
                node = node.left
            elif node.key < k:
                node = node.right
            else:
                return node
        return None

    def get_at(self, pos):
        x = pos + 1
        node = self._tree
        while node:
            if x < node.num_left:
                node = node.left
            elif node.num_left < x:
                x -= node.num_left
                node = node.right
            else:
                return (node.key, node.value)
        raise IndexError("Out of ranges")

    @staticmethod
    def _is_left(node):
        return node.parent.left and node.parent.left == node

    @staticmethod
    def _is_leaf(node):
        return node.left is None and node.right is None

    def _rotate_right(self, node):
        if not node.parent:
            self._tree = node.left
            node.left.parent = None
        elif AvlTree._is_left(node):
            node.parent.left = node.left
            node.left.parent = node.parent
        else:
            node.parent.right = node.left
            node.left.parent = node.parent
        bk = node.left.right
        node.left.right = node
        node.parent = node.left
        node.left = bk
        if bk:
            bk.parent = node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        node.num_total = 1 + self.get_num_total(node.left) + self.get_num_total(node.right)
        node.num_left = 1 + self.get_num_total(node.left)

    def _rotate_left(self, node):
        if not node.parent:
            self._tree = node.right
            node.right.parent = None
        elif AvlTree._is_left(node):
            node.parent.left = node.right
            node.right.parent = node.parent
        else:
            node.parent.right = node.right
            node.right.parent = node.parent
        bk = node.right.left
        node.right.left = node
        node.parent = node.right
        node.right = bk
        if bk:
            bk.parent = node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        node.num_total = 1 + self.get_num_total(node.left) + self.get_num_total(node.right)
        node.num_left = 1 + self.get_num_total(node.left)

    @staticmethod
    def _get_next(node):
        if not node.right:
            return node.parent
        n = node.right
        while n.left:
            n = n.left
        return n


class SegmentTree1:
    def __init__(self, data, default=2**51, func=lambda a, b: a & b):
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
        nextArr = [0] * (n + 1 - len(self.invModulos))
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
        nextArr = [0] * (n + 1 - len(self.invFactorial_))
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


def powm(a, n, m):
    if a == 1 or n == 0:
        return 1
    if n % 2 == 0:
        s = powm(a, n // 2, m)
        return s * s % m
    else:
        return a * powm(a, n - 1, m) % m


def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pairs)]
    return z


def product(l):
    por = 1
    for i in range(len(l)):
        por *= l[i]
    return por


def binarySearchCount(arr, n, key):
    left = 0
    right = n - 1
    count = 0
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] < key:
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return count


def countdig(n):
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c


def binary(x, length):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y


def countGreater(arr, n, k):
    l = 0
    r = n - 1
    leftGreater = n
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] >= k:
            leftGreater = m
            r = m - 1
        else:
            l = m + 1
    return n - leftGreater


def main(n):
    """
    n: problem scale. Here we interpret it as the number of distinct card types.
    We will generate:
      - k: max copies usable per type, between 1 and min(5, n)
      - cards: list of length n*k, values in [1, n]
      - l: list of length n, values in [1, n]
      - h: list of length k+1, h[0] unused (same as original code expecting h[0]=0 after shift)
    Then we run the original DP logic and print the resulting ans.
    """
    if n <= 0:
        print(0)
        return

    # Generate parameters
    k = random.randint(1, max(1, min(5, n)))  # keep k fairly small so DP is manageable

    # cards: length n * k, values between 1 and n
    cards = [random.randint(1, n) for _ in range(n * k)]

    # l: length n, values between 1 and n
    l = [random.randint(1, n) for _ in range(n)]

    # h: benefit array, length k+1; we will make h[0] = 0 after shifting as in original
    raw_h = [random.randint(0, 10) for _ in range(k)]  # generate k values for h[1..k]
    h = [0] + raw_h  # so that h[t] is defined for t in [0..k]

    count = defaultdict(int)
    rt = defaultdict(int)

    def find(x, y):
        # x = rt[i], y = count[i] in original
        dp = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
        for i in range(1, x + 1):
            for j in range(y + 1):
                # t: how many for this group (0..k, but cannot exceed j)
                for t in range(min(j + 1, k + 1)):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - t] + h[t])
        return dp[x][y]

    for v in cards:
        count[v] += 1
    for v in l:
        rt[v] += 1

    ans = 0
    for key in rt:
        if count[key] == 0:
            continue
        ans += find(rt[key], count[key])

    print(ans)


if __name__ == "__main__":
    # example run with some scale, e.g., n = 5
    main(5)
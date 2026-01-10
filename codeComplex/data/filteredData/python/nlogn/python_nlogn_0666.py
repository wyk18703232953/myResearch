def main(n):
    import typing as Tp

    T = Tp.TypeVar('T')

    class FenwickSum(Tp.Generic[T]):
        __slots__ = ['nodes', 'size', 'unit']

        def __init__(self, size: int, default: T, unit: T):
            self.nodes = [default] * (size + 1)
            self.size = size + 1
            self.unit = unit

        def add(self, index: int, value: T):
            while index < self.size:
                self.nodes[index] += value
                index += index & -index

        def sum(self, right: int) -> T:
            result = self.unit
            while right:
                result += self.nodes[right]
                right -= right & -right
            return result

    # Deterministic data generation for time-complexity experiments
    # n represents the length of array a
    if n <= 0:
        print(0)
        return

    # Construct a with a deterministic pattern including -1s and permutations
    # Pattern: first half positive, second half mostly -1 with some structured positives
    a = [0] * n
    half = n // 2
    # First half: permutation of 1..half
    for i in range(half):
        a[i] = (i % half) + 1 if half > 0 else 1
    # Second half: mix of -1 and values in [1, n]
    for i in range(half, n):
        if (i - half) % 3 == 0:
            a[i] = -1
        else:
            a[i] = (i % n) + 1

    mod = 998244353
    b = [x for x in a if x != -1]
    minus = n - len(b)
    if minus == 0:
        # Avoid division by zero; just run the rest logically
        # In original problem, minus>0 is usually guaranteed; here just handle gracefully
        print(0)
        return

    m_inv = pow(minus, mod - 2, mod)
    ans = 0

    bit = FenwickSum[int](n, 0, 0)
    for x in reversed(b):
        if 1 <= x <= n:
            ans += bit.sum(x)
            bit.add(x, 1)

    ans += minus * (minus - 1) * pow(4, mod - 2, mod) % mod

    acc_u, m = [0] * (n + 1), minus
    for x in a:
        if x == -1:
            m -= 1
        elif 1 <= x <= n:
            acc_u[x] = m

    for i in range(n - 1, 0, -1):
        acc_u[i] += acc_u[i + 1]
        if acc_u[i] >= mod:
            acc_u[i] -= mod

    acc_d, m = [0] * (n + 1), minus
    for x in reversed(a):
        if x == -1:
            m -= 1
        elif 1 <= x <= n:
            acc_d[x] = m

    for i in range(1, n + 1):
        acc_d[i] += acc_d[i - 1]
        if acc_d[i] >= mod:
            acc_d[i] -= mod

    present = set(b)
    for x in range(1, n + 1):
        if x not in present:
            ans = (ans + (acc_u[x] + acc_d[x]) * m_inv) % mod

    print(ans % mod)


if __name__ == "__main__":
    main(10)
class DisjointSet:
    def __init__(self, n):
        self._fa = list(range(n))

    def union(self, x, y):
        x = self.get_father(x)
        y = self.get_father(y)
        self._fa[x] = y
        return y

    def get_father(self, x):
        y = self._fa[x]
        if self._fa[y] == y:
            return y
        else:
            z = self._fa[y] = self.get_father(y)
            return z

    def __repr__(self):
        return repr([self.get_father(i) for i in range(len(self._fa))])


def solve(n, a, b, xs):
    h = {x: i for i, x in enumerate(xs)}
    if a == b:
        if all(a - x in h for x in xs):
            return [0] * n
        return False
    g1 = n
    g2 = n + 1
    ds = DisjointSet(n + 2)

    for i, x in enumerate(xs):
        for t in (a, b):
            if t - x in h:
                ds.union(i, h[t - x])

    for i, x in enumerate(xs):
        b1 = (a - x) in h
        b2 = (b - x) in h
        if b1 + b2 == 0:
            return False
        if b1 + b2 == 1:
            if b1:
                ds.union(i, g1)
            else:
                ds.union(i, g2)
            if ds.get_father(g1) == ds.get_father(g2):
                return False
    group = [None] * n
    for i, x in enumerate(xs):
        f = ds.get_father(i)
        if f < n:
            return False
        group[i] = f - n
    return group


def main(n):
    # 生成测试数据：
    # 构造 xs 使其大概率有解：
    # 选取 a, b，生成前 n//2 个元素配成和为 a，后 n-n//2 个配成和为 b
    # 再打乱顺序（这里简单起见不打乱也可以）
    if n < 2:
        # 最小规模时给一个简单数据
        a, b = 4, 7
        xs = [1] * n
    else:
        a, b = 10, 20
        xs = []
        half = n // 2

        # 为 a 构造若干对 (i, a-i)
        x = 1
        for _ in range(half // 2):
            xs.append(x)
            xs.append(a - x)
            x += 1

        # 如果 half 为奇数，多补一个自配对或任意数
        if len(xs) < half:
            xs.append(a // 2 if a % 2 == 0 else 1)

        # 为 b 构造剩下的元素
        remain = n - len(xs)
        y = 2
        for _ in range(remain // 2):
            xs.append(y)
            xs.append(b - y)
            y += 1
        if len(xs) < n:
            xs.append(b // 2 if b % 2 == 0 else 2)

        xs = xs[:n]

    group = solve(n, a, b, xs)
    if isinstance(group, list):
        print('YES')
        print('n =', n)
        print('a =', a, 'b =', b)
        print('xs =', ' '.join(map(str, xs)))
        print('group =', ' '.join(map(str, group)))
    else:
        print('NO')
        print('n =', n)
        print('a =', a, 'b =', b)
        print('xs =', ' '.join(map(str, xs)))


if __name__ == "__main__":
    # 示例调用：规模为 10
    main(10)
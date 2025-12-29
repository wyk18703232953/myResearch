import random
from collections import defaultdict

mod = 10 ** 9 + 7
mod1 = 998244353


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


def main(n: int):
    """
    使用规模 n 生成测试数据并执行原逻辑：
    - n: 数组长度
    - 生成数组 l，元素在 [0, n] 内
    - 生成 q 个区间询问，q = max(1, n//2)
    输出每次询问的结果（"even"/"odd"）
    """
    random.seed(0)

    # 生成数组 l，值域保证在树状数组有效范围内
    l = [random.randint(0, n) for _ in range(n)]

    fi = ["even", "odd"]
    q = defaultdict(int)  # 原代码中没实际用到，保留结构

    # 线段树大小为 n+1，对应下标 [0..n]
    e = [0] * (n + 1)
    s = SegmentTree(e)

    # 计算初始逆序对数（或类似统计量）
    ans = 0
    for j in range(n):
        # 查询 (l[j]+1 .. n) 区间内已有元素个数
        if l[j] + 1 <= n:
            ans += s.query(l[j] + 1, n)
        if 0 <= l[j] <= n:
            s[l[j]] = 1

    fi1 = ans

    # 生成测试用的询问数量
    num_queries = max(1, n // 2)
    outputs = []
    for _ in range(num_queries):
        # 随机生成合法区间 [a, b]
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        if a > b:
            a, b = b, a
        # 原逻辑：根据区间长度更新 fi1，并输出奇偶性
        fi1 += ((b - a + 1) * (b - a)) // 2
        outputs.append(fi[fi1 % 2])

    # 输出结果
    for o in outputs:
        print(o)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)
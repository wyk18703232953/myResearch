import os
from io import BytesIO, IOBase


BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2)
            self.buffer.write(b)
            self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2)
            self.buffer.write(b)
            self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0)
            self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


class union_find:
    def __init__(self, n):
        self.n = n
        self.rank = [0] * n
        self.parent = [int(j) for j in range(n)]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if self.rank[i] == self.rank[j]:
            self.parent[i] = j
            self.rank[j] += 1
        elif self.rank[i] > self.rank[j]:
            self.parent[j] = i

        else:
            self.parent[i] = j

    def find(self, i):
        temp = i
        if self.parent[temp] != temp:
            self.parent[temp] = self.find(self.parent[temp])
        return self.parent[temp]


def main(n):
    # 映射规模 n 到 p, q, r 和数组长度
    p = max(0, n // 3)
    q = max(0, n // 3)
    r = max(0, n - p - q)
    # 生成确定性数据
    a = [(i + 1) for i in range(p)]
    b = [(i + 2) for i in range(q)]
    c = [(i + 3) for i in range(r)]
    a.sort()
    b.sort()
    c.sort()
    l = [a, b, c]
    dp = [[[0 for _ in range(r + 1)] for _ in range(q + 1)] for _ in range(p + 1)]
    for i in range(p + 1):
        for j in range(q + 1):
            for k in range(r + 1):
                s = [i - 1, j - 1, k - 1]
                for u in range(3):
                    s[u] += 1
                    try:
                        tmp = dp[s[0]][s[1]][s[2]]
                    except Exception:
                        s[u] -= 1
                        continue
                    tmp2 = 1
                    flag = True
                    for t in range(3):
                        if u != t:
                            if s[t] == -1:
                                flag = False
                                break
                            tmp2 *= l[t][s[t]]
                    tmp += tmp2
                    s[u] -= 1
                    if flag:
                        dp[i][j][k] = max(dp[i][j][k], tmp)
    # 使用原有 FastIO 的输出路径
    out = IOWrapper(sys.stdout)
    out.write(str(dp[p][q][r]) + "\n")
    out.flush()


if __name__ == "__main__":
    import sys
    # 示例调用：可以根据需要修改 n
    main(10)
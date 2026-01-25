import sys, os, io
from collections import Counter

def run_logic(n, x, a):
    d = Counter(a)
    sa = set(a)
    if len(sa) < n:
        print(0)
    else:
        c = 0
        for i in a:
            k = i & x
            if k != i and k in d:
                c = 1
                print(1)
                break
        if c == 0:
            z = []
            for i in a:
                z.append(i & x)
            if len(set(z)) < n:
                print(2)
            else:
                print(-1)

def main(n):
    # 映射规则：
    # n: 数组长度
    # 生成方式完全确定性
    length = max(1, n)
    x = n  # 位与掩码用 n 本身
    a = [(i * 2 + (n % 3)) for i in range(length)]
    run_logic(length, x, a)

class FastWriter(io.IOBase):
    def __init__(self, fd):
        self._fd = fd
        self.buffer = io.BytesIO()
        self.write = self.buffer.write
    def flush(self):
        os.write(self._fd, self.buffer.getvalue())
        self.buffer.truncate(0)
        self.buffer.seek(0)

class FastStdout(io.IOBase):
    def __init__(self, fd=1):
        self.buffer = FastWriter(fd)
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.flush = self.buffer.flush

if __name__ == "__main__":
    sys.stdout = FastStdout()
    main(10)
    sys.stdout.flush()
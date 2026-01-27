import os
import sys
from io import BytesIO, IOBase

def main(n):
    # Deterministic data generation based on n
    # Interpret n as the length of the array a
    if n < 1:
        n = 1
    max_val = 500000
    # Choose c deterministically; keep it within value range used in a
    c = (n % max_val) + 1
    # Generate array a of length n with values in [1, max_val]
    # Pattern: a[i] = (i * 37) % max_val + 1
    a = [((i * 37) % max_val) + 1 for i in range(n)]

    nums = [[0] for _ in range(500001)]
    freq = [0] * 500001
    minus = 0
    for i in a:
        if i == c:
            minus += 1

        else:
            freq[i] += 1
            nums[i].append(freq[i] - minus)
    tot = minus
    suff = [i[:] for i in nums]
    for i in range(500001):
        for j in range(len(nums[i]) - 2, 0, -1):
            suff[i][j] = max(suff[i][j], suff[i][j + 1])
    freq = [0] * 500001
    ans = tot
    for i in a:
        if i == c:
            continue
        freq[i] += 1
        ans = max(ans, suff[i][freq[i]] - nums[i][freq[i]] + 1 + tot)
    # print(ans)
    pass

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
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

if __name__ == "__main__":
    # Example deterministic call; change n as needed for experiments
    main(1000)
import sys, os, io
from collections import Counter

def transform_string(s: str) -> str:
    d = Counter(s)
    if '1' in d:
        news = ""
        for ch in s:
            if ch != '1':
                news += ch
        ind = len(news)
        for i in range(len(news)):
            if news[i] == '2':
                ind = i
                break
        ans = news[0:ind] + '1' * d['1'] + news[ind:]
        return ans
    else:
        return s

def generate_input_string(n: int) -> str:
    if n <= 0:
        return ""
    chars = []
    base = "120"
    for i in range(n):
        chars.append(base[i % len(base)])
    return "".join(chars)

def main(n: int):
    s = generate_input_string(n)
    result = transform_string(s)
    sys.stdout.write(result + "\n")

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
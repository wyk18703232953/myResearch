import math
from collections import defaultdict, deque

def main(n):
    # Map n to problem parameters:
    # n: length of string st
    # k: number of repetitions (bounded to keep size reasonable)
    if n <= 0:
        return
    k = max(1, min(n, 10**6))

    # Deterministically generate st of length n
    # Example: periodic over lowercase letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    st = "".join(alphabet[i % 26] for i in range(n))

    res = st
    pos = 1
    cnt = 1
    while cnt < k:
        suffix = 0
        counter = 0
        for i in range(pos, len(res)):
            if res[i] == st[suffix]:
                suffix += 1

            else:
                counter = 1
                break
        if counter:
            pos += 1
            continue
        if pos > len(res):
            res += st
            cnt += 1
            pos += 1
            continue
        res += st[suffix:n]
        cnt += 1
        pos += 1
    # print(res)
    pass
if __name__ == "__main__":
    main(10)
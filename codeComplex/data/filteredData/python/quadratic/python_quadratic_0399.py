import math
from collections import defaultdict, deque

def main(n):
    # Deterministic generation of n, k, and st based on input size n
    if n < 2:
        n = 2
    k = n
    # Generate a deterministic string of length n using lowercase letters
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
    print(res)


if __name__ == "__main__":
    main(10)
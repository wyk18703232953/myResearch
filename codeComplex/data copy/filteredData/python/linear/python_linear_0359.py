from math import sqrt, log2
from collections import Counter

def process(n_str):
    ct = 0
    i = 0
    s = []
    while i < len(n_str):
        if not int(n_str[i]) % 3:
            ct += 1
            s.clear()

        else:
            t = int(n_str[i]) % 3
            if 3 - t in s:
                ct += 1
                s.clear()

            else:
                s.append(t)
        if len(s) == 3:
            ct += 1
            s.clear()
        i += 1
    return ct

def main(n):
    if n <= 0:
        test_str = "0"

    else:
        test_str = "".join(str((i % 10)) for i in range(1, n + 1))
    result = process(test_str)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)
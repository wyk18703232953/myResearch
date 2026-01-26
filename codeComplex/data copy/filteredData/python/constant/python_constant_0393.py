import itertools
import bisect
import math
from collections import *


def main(n):
    # Generate two deterministic binary strings of length n
    # Pattern: a[i] and b[i] depend on i in a fixed way
    a = [('0' if (i % 3 == 0 or i % 5 == 0) else '1') for i in range(n)]
    b = [('0' if (i % 2 == 0 or i % 7 == 0) else '1') for i in range(n)]

    ans = 0
    for i in range(n):
        if a[i] == "0":
            ans += 1
            if i - 1 >= 0 and a[i] == b[i] == b[i - 1]:
                a[i] = b[i] = b[i - 1] = "X"
            elif i + 1 < n and b[i] == b[i + 1] == a[i + 1] == a[i]:
                a[i] = b[i] = a[i + 1] = "X"
            elif i + 1 < n and a[i] == b[i] == b[i + 1]:
                a[i] = b[i] = b[i + 1] = "X"
            elif i + 1 < n and a[i] == b[i + 1] == a[i + 1]:
                a[i] = b[i + 1] = a[i + 1] = "X"
            elif i + 1 < n and a[i] == b[i] == a[i + 1]:
                a[i] = b[i] = a[i + 1] = "X"

            else:
                ans -= 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
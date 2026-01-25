from math import ceil, floor, gcd, log, log2, factorial
from collections import *

maxx = float('inf')


def transform(s: str) -> str:
    ans = s.replace('1', '') + '2'
    t = ans.find('2')
    return ans[:t] + '1' * s.count('1') + ans[t:len(ans) - 1]


def main(n: int):
    if n <= 0:
        return
    s = ''.join('1' if i % 2 == 0 else '0' for i in range(n))
    result = transform(s)
    print(result)


if __name__ == "__main__":
    main(10)
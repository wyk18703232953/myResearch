import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter
from collections import Counter

if __name__ == '__main__':
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    a, b, c, n = P()

    if a < c or b < c:
        r = -1
    else:
        r = n - (a + b - c)
    print(-1 if r <= 0 else r)
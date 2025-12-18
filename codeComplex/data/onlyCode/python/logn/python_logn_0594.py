import math
import sys
from collections import deque


def scan() -> list:
    return list(map(int, sys.stdin.readline().strip().split()))


def solution() -> None:
    # for _ in range(int(input())):
    n, k = scan()
    print(round(n+1.5-math.sqrt(2*(n+k)+2.75)))


if __name__ == '__main__':
    solution()

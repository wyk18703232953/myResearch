import sys
from collections import defaultdict
#input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    cand = 0
    tot = 0
    p = 0
    while tot < k or tot-(n-p) != k:
        cand += 1
        tot += cand
        p += 1

    print(tot-k)


if __name__ == '__main__':
    main()

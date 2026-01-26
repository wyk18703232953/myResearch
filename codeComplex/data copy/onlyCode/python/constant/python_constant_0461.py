import sys

if __name__ == '__main__':
    cin = sys.stdin

    n = int(next(cin))
    ax, ay = map(int, next(cin).split())
    bx, by = map(int, next(cin).split())
    cx, cy = map(int, next(cin).split())

#   if cx == ax or cy == ay or cx-cy==ax-ay or cx+cy==ax+ay:
#       print('YES')
#       sys.exit(0)
    if (ax-bx)*(ax-cx) > 0 and (ay-by)*(ay-cy) > 0:
        print('YES')
    else:
        print('NO')

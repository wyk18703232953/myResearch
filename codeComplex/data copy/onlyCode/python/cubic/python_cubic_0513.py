import sys
sys.stderr = sys.stdout

from math import inf


def explorer(n, m, k, R, C):
    if k % 2:
        return None

    G = [[0] * m for _ in range(n)]
    G_ = [[0] * m for _ in range(n)]
    for _ in range(k // 2):
        for i in range(n):
            for j in range(m):
                x = inf
                if i > 0:
                    x = min(x, G[i-1][j] + 2*C[i-1][j])
                if i + 1 < n:
                    x = min(x, G[i+1][j] + 2*C[i][j])
                if j > 0:
                    x = min(x, G[i][j-1] + 2*R[i][j-1])
                if j + 1 < m:
                    x = min(x, G[i][j+1] + 2*R[i][j])
                G_[i][j] = x
        G, G_ = G_, G
    return G


def main():
    n, m, k = readinti()
    R = readintll(n)
    C = readintll(n-1)
    G = explorer(n, m, k, R, C)
    if G:
        print(llstr(G))
    else:
        s = ' '.join('-1' for _ in range(m))
        print('\n'.join(s for _ in range(n)))

##########

def readint():
    return int(input())


def readinti():
   return map(int, input().split())


def readintt():
   return tuple(readinti())


def readintl():
   return list(readinti())


def readinttl(k):
    return [readintt() for _ in range(k)]


def readintll(k):
    return [readintl() for _ in range(k)]

def lstr(l):
    return ' '.join(map(str, l))

def llstr(ll):
    return '\n'.join(map(lstr, ll))


def log(*args, **kwargs):
    print(*args, **kwargs, file=sys.__stderr__)


if __name__ == '__main__':
    main()

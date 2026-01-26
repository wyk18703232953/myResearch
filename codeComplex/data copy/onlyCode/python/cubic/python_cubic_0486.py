import math


def read_ints():
    return map(int, input().split())


def read_matrix(n):
    return [list(read_ints()) for _ in range(n)]


def around(x, y, hor, ver, mtx):
    a, b, c, d = [math.inf]*4
    
    if x > 0: 
        a = hor[y][x - 1] * 2 + mtx[y][x - 1]
    
    if x < m - 1: 
        b = hor[y][x] * 2 + mtx[y][x + 1]
    
    if y > 0: 
        c = ver[y - 1][x] * 2 + mtx[y - 1][x]
    
    if y < n - 1: 
        d = ver[y][x] * 2 + mtx[y + 1][x]
    
    return min(a, b, c, d)
    

if __name__ == "__main__":
    n, m, k = read_ints()
    hor = read_matrix(n)
    ver = read_matrix(n - 1)

    if k % 2:
        for i in range(n): 
            print('-1 ' * m)
        exit()
    
    _old = [[0] * m for _ in range(n)]
    for i in range(k // 2):
        _new = [[0] * m for _ in ' ' * n]
 
        for x in range(m):
            for y in range(n):
                _new[y][x] = around(x, y, hor, ver, _old)
 
        _old = _new
 
    for row in _old: 
        print(*row)
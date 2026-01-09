def rotate(s, N):
    ret = [[None for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[i][j] = s[j][N-1-i]
    return ret

def v_mirror(s):
    return list(reversed(s))

def h_mirror(s):
    return [list(reversed(row)) for row in s]

def solve(s1, s2, N):
    cur = s1
    for _ in range(4):
        if cur == s2:
            return True
        if v_mirror(cur) == s2:
            return True
        if h_mirror(cur) == s2:
            return True
        if v_mirror(h_mirror(cur)) == s2:
            return True
        cur = rotate(cur, N)
    return False

def main(n):
    N = max(1, n)
    s1 = [[chr(ord('a') + (i + j) % 26) for j in range(N)] for i in range(N)]
    s2 = [[chr(ord('a') + (i * 2 + j * 3) % 26) for j in range(N)] for i in range(N)]
    res = solve(s1, s2, N)
    # print('Yes' if res else 'No')
    pass
if __name__ == "__main__":
    main(5)
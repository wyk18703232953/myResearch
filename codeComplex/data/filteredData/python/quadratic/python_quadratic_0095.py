def rotate(s, N):
    ret = [[None for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[i][j] = s[j][N - 1 - i]
    return ret

def v_mirror(s):
    return list(reversed(s))

def h_mirror(s):
    return [list(reversed(row)) for row in s]

def solve(s1, s2, N):
    current = s1
    for _ in range(4):
        if current == s2:
            return True
        if v_mirror(current) == s2:
            return True
        if h_mirror(current) == s2:
            return True
        if v_mirror(h_mirror(current)) == s2:
            return True
        current = rotate(current, N)
    return False

def generate_matrix(N, offset):
    # Deterministic pattern: characters depend on (i, j, offset)
    # Use lowercase letters mapped from a simple arithmetic expression
    return [[chr(ord('a') + (i * N + j + offset) % 26) for j in range(N)] for i in range(N)]

def main(n):
    if n <= 0:
        return
    N = n
    s1 = generate_matrix(N, 0)
    s2 = rotate(s1, N)
    result = solve(s1, s2, N)
    print('Yes' if result else 'No')

if __name__ == "__main__":
    main(5)
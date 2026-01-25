def flipH(A, N):
    B = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            B[i][j] = A[i][N - j - 1]
    return B

def flipV(A, N):
    B = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            B[i][j] = A[N - i - 1][j]
    return B

def rotate90(A):
    ans = zip(*A[::-1])
    ans = list(map(list, ans))
    return ans

def check(A, B, N):
    for i in range(N):
        for j in range(N):
            if A[i][j] != B[i][j]:
                return False
    return True

def generate_matrix(N):
    chars = ['a', 'b', 'c', 'd']
    M = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(chars[(i * N + j) % len(chars)])
        M.append(row)
    return M

def main(n):
    N = max(1, n)
    A = generate_matrix(N)
    # deterministically choose X as either a transformed version of A or unchanged
    if N % 4 == 0:
        X = flipH(A, N)
    elif N % 4 == 1:
        X = flipV(A, N)
    elif N % 4 == 2:
        X = rotate90(A)
    else:
        X = [row[:] for row in A]

    B = flipH(A, N)
    C = flipV(A, N)
    flag = False
    for _ in range(4):
        if check(A, X, N) or check(B, X, N) or check(C, X, N):
            flag = True
            break
        else:
            A = rotate90(A)
            B = rotate90(B)
            C = rotate90(C)
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main(5)
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

def main(n):
    N = n
    A = []
    X = []
    for i in range(N):
        row = [chr(ord('a') + (i + j) % 26) for j in range(N)]
        A.append(row)
    for i in range(N):
        row = [chr(ord('a') + (i * 2 + j * 3) % 26) for j in range(N)]
        X.append(row)
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
        # print("Yes")
        pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    main(5)
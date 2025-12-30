import random

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

def generate_random_matrix(N):
    # 使用随机的 '0' 和 '1' 生成矩阵
    return [[random.choice(['0', '1']) for _ in range(N)] for _ in range(N)]

def transform_matrix(A, N):
    # 随机选择一种与原题逻辑一致的变换来生成 X
    choice = random.randint(0, 5)
    B = flipH(A, N)
    C = flipV(A, N)

    if choice == 0:
        return A
    elif choice == 1:
        return rotate90(A)
    elif choice == 2:
        return rotate90(rotate90(A))
    elif choice == 3:
        return rotate90(rotate90(rotate90(A)))
    elif choice == 4:
        return B
    else:
        return C

def main(n):
    N = n
    A = generate_random_matrix(N)
    X = transform_matrix(A, N)

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
    # 示例调用：规模为 4
    main(4)
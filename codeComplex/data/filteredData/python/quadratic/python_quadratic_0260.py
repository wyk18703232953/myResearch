def main(n):
    # Deterministically generate a, b from n
    # Ensure 1 <= a, b <= n
    a = n % n + 1  # always 1..n, but n%n=0 so a=1
    b = (n // 2) % n + 1

    if a > n:
        print('NO')
        return
    if b > n:
        print("NO")
        return
    if a == 1 and b == 1:
        if n == 2 or n == 3:
            print('NO')
            return
    if (n == 1 and a > 1) or (n == 1 and b > 1):
        print('NO')
        return
    if min(a, b) > 1:
        print('NO')
        return

    def check(mat):
        vis = [0] * n
        cnt = 0
        for i in range(n):
            if vis[i] == 0:
                q = [i]
                cnt += 1
                vis[i] = 1
                while q:
                    t = q.pop(0)
                    for j in range(n):
                        if mat[t][j] == 1 and vis[j] == 0:
                            vis[j] = 1
                            q.append(j)
        return cnt

    mat = [[0 for _ in range(n)] for _ in range(n)]
    m = max(a, b)
    j = 1
    for i in range(n):
        if j < n:
            mat[i][j] = 1
            mat[j][i] = 1
        j += 1
    for i in range(m - 1):
        curr = n - i - 1
        for j in range(n):
            if mat[curr][j] == 1:
                mat[curr][j] = 0
                mat[j][curr] = 0
    if b == 1:
        print('YES')
        for i in range(n):
            print(*mat[i], sep='')
    else:
        print('YES')
        for i in range(n):
            for j in range(n):
                mat[i][j] = 1 - mat[i][j]
        for i in range(n):
            mat[i][i] = 0
        for i in range(n):
            print(*mat[i], sep='')


if __name__ == "__main__":
    main(5)
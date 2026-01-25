def main(n):
    # 对于给定的规模 n，确定性地构造 a, b
    # 保证 a、b 与原程序的逻辑保持一致但无需外部输入
    a = 1 if n % 2 == 0 else 2
    b = 1 if n % 3 == 0 else 1

    if a > 1 and b > 1:
        print("NO")
        return
    if 2 <= n <= 3 and a == b == 1:
        print("NO")
        return
    print("YES")

    if b == 1:
        adj = [[0] * n for _ in range(n)]
        conn = n
        for i in range(n - 1):
            if conn == a:
                break
            adj[i][i + 1] = adj[i + 1][i] = 1
            conn -= 1
            if conn == a:
                break
    elif a == 1:
        adj = [[1] * n for _ in range(n)]
        conn = n
        for i in range(n):
            adj[i][i] = 0
        for i in range(n - 1):
            if conn == b:
                break
            adj[i][i + 1] = adj[i + 1][i] = 0
            conn -= 1
            if conn == b:
                break
    else:
        adj = [[0] * n for _ in range(n)]

    for row in adj:
        print(*row, sep='')


if __name__ == "__main__":
    main(5)
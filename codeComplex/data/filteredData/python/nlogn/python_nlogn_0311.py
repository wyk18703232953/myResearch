def main(n):
    # 构造一个确定性的排列 p（0-based），长度为 n
    # 这里采用简单的循环移位：p[i] = (i + 1) % n
    if n <= 0:
        return
    p = [(i + 1) % n for i in range(n)]

    vis = [False] * n
    odd = 0
    for x in range(n):
        if vis[x]:
            continue
        odd ^= 1
        while not vis[x]:
            odd ^= 1
            vis[x] = True
            x = p[x]

    result = 'Petr' if (n + odd) % 2 == 0 else 'Um_nik'
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：以规模 n = 10 运行
    main(10)
def main(n):
    p, u = "Petr", "Um_nik"

    # 生成一个含有 n 个元素的排列，确保是 1..n 的排列
    # 这里构造一个简单的确定性排列：将 1..n 左循环移动一位
    # perm[i] 表示位置 i+1 的值
    if n <= 0:
        return

    arr = [(i % n) + 1 for i in range(1, n + 1)]

    vis = [0] * (n + 1)
    dic = {v: i + 1 for i, v in enumerate(arr)}

    sm = 0
    for i in range(1, n + 1):
        if vis[i] == 0:
            now = i
            vis[now] = 1
            while dic[now] != i:
                sm += 1
                now = dic[now]
                vis[now] = 1
    if (3 * n - sm) % 2 == 0:
        print(p)
    else:
        print(u)


if __name__ == "__main__":
    main(10)
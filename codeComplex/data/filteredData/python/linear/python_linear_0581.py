def main(n):
    # 对应原程序中的 n, s 输入结构：
    # n: 初始的 n
    # s: 与 n 同规模的确定性构造，这里设为 n*(n+1)//2，保证算法有工作量
    if n <= 0:
        # print(0)
        pass
        return

    cur_n = n
    s = n * (n + 1) // 2

    ans = 0
    while s > 0 and cur_n > 0:
        a = s // cur_n
        s -= cur_n * a
        ans += a
        cur_n -= 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)
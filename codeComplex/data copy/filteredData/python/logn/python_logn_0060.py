def main(n):
    # 解释规模含义：
    # 将 n 映射为区间长度 len = n + 1，令 l = 0, r = n
    # 这样：(l, r) 的规模由 n 控制，且完全确定
    l = 0
    r = n

    ans = 0
    for i in range(63, -1, -1):
        if (r & (1 << i)) > 0 and (l & (1 << i)) == 0:
            ans = (1 << (i + 1)) - 1
            break
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模
    main(10)